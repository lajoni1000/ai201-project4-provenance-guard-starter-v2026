
#!/usr/bin/env python3
"""
AI201 Unit 9 - Provenance Guard Capstone Evaluation

Purpose:
    Evaluate the five acceptance criteria defined for the Unit 9 Capstone.

    Each criterion is tested three times using the same procedure.
    The evaluator records actual HTTP responses and audit log entries
    and generates a Markdown report with the results.

Acceptance criteria:
    AC1 - HTTP 400 Audit Logging
    AC2 - HTTP 429 Audit Logging
    AC3 - Audit Log Preservation
    AC4 - Request Instrumentation
    AC5 - Raw Text Protection

Existing project components:
    app.py          Flask application and HTTP endpoints
    audit.py        Audit logging functionality
    config.py       Application configuration
    scenarios.py    Existing Unit 8 validation scenarios
    run_eval.py     Existing evaluation helper
    logs/audit.jsonl    Application audit log

How to run:
    Terminal 1:
        python app.py

    Terminal 2:
        python run_eval_capstone.py

Output:
    results/capstone_run_<timestamp>.md

Important:
    This evaluator does not modify application code, configuration,
    or previously stored audit records.

    It intentionally generates new audit records by sending requests
    to the running application.
"""

import argparse
import datetime as dt
import json
import sys
import uuid

import requests

import config
import scenarios
from run_eval import bodies_for


# ------------------------------------------------------------
# ACCEPTANCE CRITERIA CONFIGURATION
# ------------------------------------------------------------

# These fields must exist in every HTTP 400 and HTTP 429
# rejection audit record.
REQUIRED_REJECTION_FIELDS = {
    "creator_id",
    "input_type",
    "text_length",
    "reason",
    "http_status",
    "timestamp",
}

# The targets below match the acceptance criteria established
# before running the formal Capstone evaluation.
CRITERIA = [
    ("HTTP 400 Audit Logging", "10/10"),
    ("HTTP 429 Audit Logging", "10/10"),
    ("Audit Log Preservation", "0 changes"),
    ("Request Instrumentation", "10/10"),
    ("Raw Text Protection", "0 exposures"),
]


# ------------------------------------------------------------
# AUDIT LOG HELPERS
# ------------------------------------------------------------

def read_log_bytes():
    """
    Read the existing audit log as raw bytes.

    Reading bytes allows us to compare the original log content
    with the content after a test.

    This function never clears, rewrites, or deletes the log.
    """
    path = config.AUDIT_LOG

    return path.read_bytes() if path.exists() else b""


def parse_new_entries(previous_size):
    """
    Return only audit entries added after a known byte position.

    This is important because audit.jsonl may already contain
    records from previous units or earlier testing.

    By reading only newly appended records, we avoid counting
    historical entries as evidence for the current request.
    """
    raw = read_log_bytes()

    # A smaller file would indicate that existing content
    # was removed or the log was replaced.
    if len(raw) < previous_size:
        raise RuntimeError(
            "Audit log became smaller during the test."
        )

    added = raw[previous_size:]

    if not added:
        return []

    # Each nonempty line in a JSONL file is a JSON object.
    return [
        json.loads(line)
        for line in added.decode("utf-8").splitlines()
        if line.strip()
    ]


def send_request(url, body, timeout):
    """
    Send one HTTP POST request to /submit.

    Before sending the request, record the audit log size.
    After receiving the response, collect only the new records.

    This links the HTTP response with the audit evidence
    generated during that request.
    """
    before_size = len(read_log_bytes())

    response = requests.post(
        f"{url}/submit",
        json=body,
        timeout=timeout,
    )

    entries = parse_new_entries(before_size)

    return {
        "status": response.status_code,
        "entries": entries,
    }


def rejection_entries(result):
    """
    Extract rejection events from one request's audit entries.

    The application may generate more than one type of audit
    event, so we filter specifically for event='rejected'.
    """
    return [
        entry
        for entry in result["entries"]
        if entry.get("event") == "rejected"
    ]


def metric_entries(result):
    """
    Extract request instrumentation events.

    These records contain the HTTP status, outcome,
    and request duration.
    """
    return [
        entry
        for entry in result["entries"]
        if entry.get("event") == "request_metrics"
    ]


# ------------------------------------------------------------
# AUDIT VALIDATION HELPERS
# ------------------------------------------------------------

def valid_rejection(result, expected_status):
    """
    Verify that one rejected request meets the audit requirements.

    A request passes only when:
        1. Its HTTP response has the expected status.
        2. Exactly one rejection event was generated.
        3. All six required fields exist.
        4. The required values are present and valid.

    This helper is reused by AC1 and AC2.
    """
    entries = rejection_entries(result)

    if result["status"] != expected_status:
        return False

    if len(entries) != 1:
        return False

    entry = entries[0]

    # Check that the six required fields exist.
    if not REQUIRED_REJECTION_FIELDS.issubset(entry):
        return False

    # None of the required fields should contain None.
    if any(
        entry[field] is None
        for field in REQUIRED_REJECTION_FIELDS
    ):
        return False

    return (
        entry["http_status"] == expected_status
        and isinstance(entry["timestamp"], str)
        and bool(entry["timestamp"])
        and isinstance(entry["reason"], str)
        and bool(entry["reason"])
        and isinstance(entry["creator_id"], str)
        and bool(entry["creator_id"])
        and isinstance(entry["input_type"], str)
        and bool(entry["input_type"])
        and isinstance(entry["text_length"], int)
        and not isinstance(entry["text_length"], bool)
        and entry["text_length"] >= 0
    )


def valid_metric(result):
    """
    Verify that one request generated correct instrumentation.

    The metric must include:
        - duration_ms >= 0
        - the actual HTTP response status
        - the expected outcome

    Expected outcomes:
        HTTP 200 -> success
        HTTP 400 -> rejected
        HTTP 429 -> rejected
    """
    metrics = metric_entries(result)

    if len(metrics) != 1:
        return False

    metric = metrics[0]
    status = result["status"]

    expected_outcome = (
        "success"
        if status == 200
        else "rejected"
        if status in (400, 429)
        else "error"
    )

    duration = metric.get("duration_ms")

    return (
        metric.get("event") == "request_metrics"
        and metric.get("http_status") == status
        and metric.get("outcome") == expected_outcome
        and isinstance(duration, (int, float))
        and not isinstance(duration, bool)
        and duration >= 0
    )


# ------------------------------------------------------------
# TEST DATA HELPERS
# ------------------------------------------------------------

def invalid_bodies(trial_id):
    """
    Reuse the ten API Input Validation scenarios from Unit 8.

    We do not create a second set of validation examples.

    Unique creator IDs prevent previous rate-limit activity
    from affecting the current trial.

    The invalid text and validation conditions remain unchanged.
    """
    scenario = next(
        item
        for item in scenarios.SCENARIOS
        if item["name"] == "API Input Validation"
    )

    bodies = []

    for index, original in enumerate(
        bodies_for(scenario), 1
    ):
        body = original.copy()

        creator = body.get("creator_id")

        # Preserve missing creator IDs because they are
        # part of the original validation test.
        if isinstance(creator, str) and creator:
            body["creator_id"] = (
                f"cap_{trial_id}_{index}"
            )

        bodies.append(body)

    if len(bodies) != 10:
        raise ValueError(
            "AC1 requires exactly ten invalid bodies."
        )

    return bodies


def trigger_rate_limit(url, timeout, trial_id, prefix):
    """
    Deliberately reach the configured per-minute rate limit.

    A unique creator ID isolates this test from other trials.

    Empty text is used because it produces a validation rejection
    without invoking the language model.

    After these setup requests, additional requests using
    the same creator ID should receive HTTP 429.
    """
    creator_id = f"cap_{prefix}_{trial_id}"

    body = {
        "creator_id": creator_id,
        "text": "",
    }

    priming = []

    # Consume the allowed number of requests.
    for _ in range(config.RATE_LIMIT_PER_MINUTE):
        priming.append(
            send_request(url, body, timeout)
        )

    return body, priming


# ------------------------------------------------------------
# AC1 - HTTP 400 AUDIT LOGGING
# ------------------------------------------------------------

def run_ac1(url, timeout, trial_id):
    """
    AC1 - HTTP 400 Audit Logging

    Target:
        10 out of 10 invalid requests must return HTTP 400
        and generate a complete rejection audit record.

    Method:
        Reuse the ten existing Unit 8 validation scenarios.

    Failure examples:
        - A request returns HTTP 500 instead of HTTP 400.
        - A rejection event is missing.
        - A required audit field is missing.
    """
    results = [
        send_request(url, body, timeout)
        for body in invalid_bodies(trial_id)
    ]

    passed = sum(
        valid_rejection(result, 400)
        for result in results
    )

    return {
        "score": f"{passed}/10",
        "met": passed == 10,
        "evidence": results,
        "source": (
            "app.py::submit, "
            "audit.py::log_rejection"
        ),
    }


# ------------------------------------------------------------
# AC2 - HTTP 429 AUDIT LOGGING
# ------------------------------------------------------------

def run_ac2(url, timeout, trial_id):
    """
    AC2 - HTTP 429 Audit Logging

    Target:
        10 out of 10 rate-limited requests must return
        HTTP 429 and generate a complete rejection audit record.

    Method:
        First consume the allowed request quota.
        Then send ten additional requests using the same ID.

    The setup requests are not counted in the AC2 score.
    """
    body, priming = trigger_rate_limit(
        url,
        timeout,
        trial_id,
        "rate",
    )

    # These requests should be blocked by the rate limiter.
    results = [
        send_request(url, body, timeout)
        for _ in range(10)
    ]

    passed = sum(
        valid_rejection(result, 429)
        for result in results
    )

    # Confirm that the setup requests did not already
    # receive HTTP 429.
    setup_ok = all(
        result["status"] == 400
        for result in priming
    )

    return {
        "score": f"{passed}/10",
        "met": passed == 10 and setup_ok,
        "evidence": results,
        "setup_statuses": [
            result["status"]
            for result in priming
        ],
        "source": (
            "app.py::rate_limited, "
            "audit.py::log_rejection"
        ),
    }


# ------------------------------------------------------------
# AC3 - AUDIT LOG PRESERVATION
# ------------------------------------------------------------

def run_ac3(url, timeout, trial_id):
    """
    AC3 - Audit Log Preservation

    Target:
        Zero modifications or deletions of existing audit records.

    Method:
        1. Capture the complete audit log before testing.
        2. Generate ten new rejected requests.
        3. Read the audit log again.
        4. Verify that the original bytes remain unchanged
           at the beginning of the file.

    New records may be appended, but historical records
    must remain intact and in their original order.
    """
    before = read_log_bytes()

    results = []

    for index in range(10):
        body = {
            "creator_id": (
                f"cap_preserve_{trial_id}_{index}"
            ),
            "text": "",
        }

        results.append(
            send_request(url, body, timeout)
        )

    after = read_log_bytes()

    # If the original log remains an exact prefix,
    # its content and ordering were preserved.
    unchanged = after.startswith(before)

    added_bytes = (
        after[len(before):]
        if unchanged
        else b""
    )

    new_rejections = sum(
        len(rejection_entries(result))
        for result in results
    )

    setup_ok = (
        len(results) == 10
        and all(
            result["status"] == 400
            for result in results
        )
        and new_rejections == 10
        and len(added_bytes) > 0
    )

    met = unchanged and setup_ok

    return {
        "score": (
            "0 changes"
            if met
            else "FAILED"
        ),
        "met": met,
        "evidence": results,
        "details": {
            "original_bytes": len(before),
            "final_bytes": len(after),
            "original_prefix_unchanged": unchanged,
            "new_rejections": new_rejections,
        },
        "source": (
            "audit.py::_append, "
            "app.py::submit"
        ),
    }


# ------------------------------------------------------------
# AC4 - REQUEST INSTRUMENTATION
# ------------------------------------------------------------

def run_ac4(url, timeout, trial_id):
    """
    AC4 - Request Instrumentation

    Target:
        10 out of 10 evaluated requests must generate
        correct request_metrics records.

    Test distribution:
        1 successful request (HTTP 200)
        4 validation rejections (HTTP 400)
        5 rate-limit rejections (HTTP 429)

    Each metric must contain:
        - duration_ms >= 0
        - the correct HTTP status
        - the correct outcome

    The successful request exercises the real model path.
    """
    results = []

    # HTTP 200: a valid submission should invoke
    # the existing detection pipeline.
    valid_body = {
        "creator_id": (
            f"cap_metric_valid_{trial_id}"
        ),
        "text": (
            "This is a sample submission used to evaluate "
            "request instrumentation in Provenance Guard."
        ),
    }

    results.append(
        send_request(url, valid_body, timeout)
    )

    # HTTP 400: four invalid submissions.
    for index in range(4):
        results.append(
            send_request(
                url,
                {
                    "creator_id": (
                        f"cap_metric_bad_{trial_id}_{index}"
                    ),
                    "text": "",
                },
                timeout,
            )
        )

    # HTTP 429: consume the quota using a separate ID.
    limited_body, priming = trigger_rate_limit(
        url,
        timeout,
        trial_id,
        "metrics",
    )

    # Send five requests that should be rate-limited.
    for _ in range(5):
        results.append(
            send_request(
                url,
                limited_body,
                timeout,
            )
        )

    expected_statuses = (
        [200]
        + [400] * 4
        + [429] * 5
    )

    actual_statuses = [
        result["status"]
        for result in results
    ]

    passed = sum(
        valid_metric(result)
        and result["status"] == expected
        for result, expected in zip(
            results,
            expected_statuses,
        )
    )

    setup_ok = all(
        result["status"] == 400
        for result in priming
    )

    return {
        "score": f"{passed}/10",
        "met": (
            passed == 10
            and actual_statuses == expected_statuses
            and setup_ok
        ),
        "evidence": results,
        "setup_statuses": [
            result["status"]
            for result in priming
        ],
        "source": (
            "app.py::after_request, "
            "audit.py::_append"
        ),
    }


# ------------------------------------------------------------
# AC5 - RAW TEXT PROTECTION
# ------------------------------------------------------------

def run_ac5(url, timeout, trial_id):
    """
    AC5 - Raw Text Protection

    Target:
        Zero exact raw-text exposures in audit records
        from ten evaluated requests.

    Method:
        Send unique text strings and inspect the audit
        entries generated by each request.

    Test distribution:
        5 valid submissions
        5 invalid submissions

    Valid submissions exercise the normal detection path.
    Invalid submissions exercise rejection logging.

    Limitation:
        This checks exact text exposure in audit records
        generated by these ten requests. It does not prove
        protection against every possible data leakage path.
    """
    results = []
    exposures = 0

    for index in range(10):

        # Unique markers make each test submission identifiable.
        marker = f"PRIVATE_{trial_id[-6:]}_{index}"

        if index < 5:
            # Valid text exercises the successful submission path.
            text = (
                f"{marker} This is a private sample submission "
                "used to evaluate audit log data minimization."
            )
            expected_status = 200
        else:
            # Short text deliberately triggers HTTP 400.
            text = marker
            expected_status = 400

        body = {
            "creator_id": (
                f"cap_privacy_{trial_id}_{index}"
            ),
            "text": text,
        }

        result = send_request(
            url,
            body,
            timeout,
        )

        results.append(result)

        # Search the actual audit entries for the complete
        # original text submitted in the request.
        serialized = json.dumps(
            result["entries"],
            ensure_ascii=False,
        )

        if text in serialized:
            exposures += 1

        # Unexpected HTTP responses make the test invalid.
        if result["status"] != expected_status:
            exposures += 1

    # Verify that each request generated the expected
    # type of audit event and its instrumentation record.
    logged_ok = all(
        len(metric_entries(result)) == 1
        and (
            len(rejection_entries(result)) == 1
            if result["status"] == 400
            else result["status"] == 200
        )
        for result in results
    )

    met = (
        exposures == 0
        and logged_ok
        and len(results) == 10
    )

    return {
        "score": f"{exposures} exposures",
        "met": met,
        "evidence": results,
        "details": {
            "requests": len(results),
            "http_200_count": sum(
                r["status"] == 200
                for r in results
            ),
            "http_400_count": sum(
                r["status"] == 400
                for r in results
            ),
            "all_requests_logged": logged_ok,
            "raw_text_exposures_or_status_failures": exposures,
        },
        "source": (
            "app.py::submit, "
            "audit.py::log_decision, "
            "audit.py::log_rejection"
        ),
    }


# ------------------------------------------------------------
# REPORT GENERATION
# ------------------------------------------------------------

def sample_output(result):
    """
    Select actual captured output for the Markdown report.

    The report contains real HTTP statuses and JSON audit
    entries produced by the application.

    For AC4, all ten results are included to show the
    different response types.

    For other criteria, two examples are included per trial.
    """
    evidence = result.get("evidence", [])

    if not evidence:
        return {
            "error": "No evidence captured"
        }

    if result["source"].startswith(
        "app.py::after_request"
    ):
        selected = evidence
    else:
        selected = evidence[:2]

    return [
        {
            "http_status": item["status"],
            "audit_entries": item["entries"],
        }
        for item in selected
    ]


def write_report(all_results, run_id):
    """
    Generate the Markdown run log required by Milestone 5.

    The report contains:
        - Five acceptance criteria
        - The target for each criterion
        - Three trial results
        - MET or MISSED verdicts
        - Actual output from the application
        - Source files and functions

    Results are written to a new file so earlier
    evaluation reports are preserved.
    """
    config.RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    path = (
        config.RESULTS_DIR
        / f"capstone_run_{run_id}.md"
    )

    lines = [
        "# Unit 9 Capstone - Evaluation Run Log",
        "",
        f"- Evaluation ID: `{run_id}`",
        "- Evaluator: `run_eval_capstone.py::main`",
        "- Service: `app.py::submit`",
        "- Audit file: `logs/audit.jsonl`",
        "- Trials: 3 per criterion",
        "- Rate-limit counters isolated using unique creator IDs",
        "",
        "| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |",
        "|---|---|---|---|---|---|",
    ]

    # Build the five-row results table.
    for index, (name, target) in enumerate(CRITERIA):
        trials = all_results[index]

        scores = [
            trial["score"]
            for trial in trials
        ]

        verdict = (
            "MET"
            if all(
                trial["met"]
                for trial in trials
            )
            else "MISSED"
        )

        lines.append(
            f"| {index + 1}. {name} | {target} | "
            f"{scores[0]} | {scores[1]} | {scores[2]} | "
            f"{verdict} |"
        )

    lines.extend([
        "",
        "## Real Output and Evidence",
        "",
        "The JSON below was captured from actual HTTP requests",
        "and audit records generated by Provenance Guard.",
        "",
    ])

    # Add evidence for every criterion and every trial.
    for index, (name, _) in enumerate(CRITERIA):
        lines.append(
            f"### AC{index + 1} - {name}"
        )
        lines.append("")

        for trial_number, result in enumerate(
            all_results[index], 1
        ):
            lines.append(
                f"**Trial {trial_number}: "
                f"{result['score']}**"
            )
            lines.append("")

            lines.append(
                f"Produced by: `{result['source']}`"
            )
            lines.append("")

            # Include additional verification details
            # when a criterion provides them.
            if "details" in result:
                lines.append(
                    "Verification details:"
                )
                lines.append("")
                lines.append("```json")
                lines.append(
                    json.dumps(
                        result["details"],
                        indent=2,
                    )
                )
                lines.append("```")
                lines.append("")

            # Show the requests used to prepare rate-limit tests.
            if "setup_statuses" in result:
                lines.append(
                    "Rate-limit setup HTTP statuses: "
                    + str(result["setup_statuses"])
                )
                lines.append("")

            # Include actual captured HTTP and audit output.
            lines.append(
                "Actual captured output:"
            )
            lines.append("")
            lines.append("```json")
            lines.append(
                json.dumps(
                    sample_output(result),
                    indent=2,
                    ensure_ascii=False,
                )
            )
            lines.append("```")
            lines.append("")

    path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    return path


# ------------------------------------------------------------
# MAIN EVALUATION WORKFLOW
# ------------------------------------------------------------

def main():
    """
    Execute the complete Capstone evaluation.

    Workflow:
        1. Validate the test environment.
        2. Confirm that the Flask service is available.
        3. Run all five criteria three times.
        4. Record actual results.
        5. Generate the Markdown report.
        6. Display final MET/MISSED verdicts.

    The application code and acceptance criteria remain
    unchanged between trials.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate the five Unit 9 Capstone criteria."
        )
    )

    parser.add_argument(
        "--url",
        default=(
            f"http://{config.HOST}:{config.PORT}"
        ),
        help="Base URL of the running Flask service.",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=120,
        help="Request timeout in seconds.",
    )

    args = parser.parse_args()

    # Rate limiting must be enabled to evaluate HTTP 429.
    if not config.RATE_LIMITING_ENABLED:
        sys.exit(
            "Rate limiting must be enabled for AC2 and AC4."
        )

    if config.RATE_LIMIT_PER_MINUTE < 1:
        sys.exit(
            "Invalid rate-limit configuration."
        )

    # Confirm that the existing Unit 8 scenarios are valid.
    problems = scenarios.validate()

    if problems:
        sys.exit(
            "Invalid scenarios.py: "
            + "; ".join(problems)
        )

    # Verify that the application is running before testing.
    try:
        response = requests.get(
            f"{args.url}/health",
            timeout=5,
        )

        response.raise_for_status()

    except requests.RequestException as exc:
        sys.exit(
            f"Cannot reach Provenance Guard at "
            f"{args.url}: {exc}\n"
            "Start the service first with: python app.py"
        )

    # Use a timestamp and random suffix to identify
    # this evaluation and prevent ID collisions.
    run_id = (
        dt.datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + "_"
        + uuid.uuid4().hex[:6]
    )

    # Each acceptance criterion has one test function.
    tests = [
        run_ac1,
        run_ac2,
        run_ac3,
        run_ac4,
        run_ac5,
    ]

    all_results = [
        [] for _ in CRITERIA
    ]

    print(
        "\nAI201 - Unit 9 Capstone Evaluation"
    )
    print(
        "Five criteria, three trials each"
    )
    print(
        f"Evaluation ID: {run_id}\n"
    )

    try:
        # Run three independent trials.
        # Do not change application code or configuration
        # between trials.
        for trial_number in range(1, 4):

            print(
                f"=== TRIAL {trial_number} ==="
            )

            trial_id = (
                f"{run_id}_t{trial_number}"
            )

            # Execute all five criteria in each trial.
            for index, test in enumerate(tests):

                name = CRITERIA[index][0]

                result = test(
                    args.url,
                    args.timeout,
                    trial_id,
                )

                all_results[index].append(
                    result
                )

                print(
                    f"AC{index + 1}: {name}: "
                    f"{result['score']} - "
                    f"{'MET' if result['met'] else 'MISSED'}"
                )

            print()

    except (
        requests.RequestException,
        RuntimeError,
        ValueError,
    ) as exc:

        print(
            f"\nEvaluation interrupted: {exc}",
            file=sys.stderr,
        )

        print(
            "Do not report incomplete trials as completed.",
            file=sys.stderr,
        )

        sys.exit(1)

    # Save the complete evaluation results.
    path = write_report(
        all_results,
        run_id,
    )

    print(
        "=== FINAL VERDICTS ==="
    )

    for index, (name, _) in enumerate(CRITERIA):

        verdict = (
            "MET"
            if all(
                result["met"]
                for result in all_results[index]
            )
            else "MISSED"
        )

        print(
            f"AC{index + 1}: "
            f"{name}: {verdict}"
        )

    print(
        f"\nReport saved to: {path}"
    )


# Execute the evaluation only when this file is
# run directly, not when imported by another module.
if __name__ == "__main__":
    main()
