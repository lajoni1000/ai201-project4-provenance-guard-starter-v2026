# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False Positive Protection

<!-- Your criterion. It must name a number. -->
No more than 1 out of 10 verified human-written texts should receive a high-confidence AI label.

Test: Submit 10 verified human-written texts to /submit, including formal writing and writing by non-native English speakers. Count how many receive the high-confidence AI label. The target must be met in each of the three evaluation trials.

**Why this target:**
I chose a maximum of 1 false positive out of 10 because falsely accusing someone of using AI can be more harmful than missing an AI-generated text. This is especially important for people whose writing style may be misinterpreted by the detection signals.


---

## 2. AI-Generated Text Detection

<!-- Your criterion. -->
At least 8 out of 10 verified AI-generated texts should receive a high-confidence AI label.

Test: Submit 10 AI-generated texts covering different topics and writing styles to /submit. Count how many receive the high-confidence AI label. The target must be met in each of the three evaluation trials.

**Why this target:**
 I chose 8 out of 10 because I want the system to identify most AI-generated texts while allowing for cases where the detection signals cannot confidently recognize them. Requiring 100% detection could encourage thresholds that increase false accusations.


---

## 3. Signal Disagreement Handling

<!-- Your criterion. -->
All 10 predefined cases where the two signals strongly disagree should produce the unsure classification.

Test: Create 10 pairs of model and style scores where one score is at least 0.80 and the other is at most 0.20. Pass each pair through the combining and label-mapping logic and verify that all 10 produce unsure. Repeat across three trials.

**Why this target:**
I chose 10 out of 10 because when the model and stylometry signals strongly disagree, the system should consistently return unsure. A confident classification in these situations could be misleading, especially when one signal produces a false positive.


---

## 4. Appeal Process

<!-- Your criterion. -->
All 10 valid appeals should be recorded, assigned under_review, and linked to the correct submission without changing the original classification.

Test: Submit 10 texts and save their content_id values. Submit an appeal for each one using /appeal with a reasoning message. Verify the appeal status, submission link, original classification, and audit log entry. Repeat across three trials.

**Why this target:**
I chose 10 out of 10 because every valid appeal should be recorded and linked to the correct submission. Missing even one appeal could prevent someone from challenging an incorrect classification.


---

## 5. API Input Validation

<!-- Your criterion. -->
The system should correctly reject 10 out of 10 invalid requests without crashing or creating a classification.

Test: Send 10 invalid requests to the /submit endpoint, including missing text, empty text, missing creator ID, and incorrect data types. Verify that each request returns HTTP 400 Bad Request with an error message. Repeat across three trials.

**Why this target:**
  I chose 10 out of 10 because invalid requests should not produce classifications. Validating the input helps prevent unreliable results and unnecessary processing by the detection signals.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
