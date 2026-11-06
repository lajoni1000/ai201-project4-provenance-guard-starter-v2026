# Run log — before_complete

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-05 22:28

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False Positive Protection | ≤1/10 high-confidence AI labels | 3/10 | 3/10 | 3/10 | MISSED |
| 2. AI-Generated Text Detection | ≥8/10 high-confidence AI labels | 2/10 | 2/10 | 2/10 | MISSED |
| 3. Signal Disagreement Handling | 10/10 labeled unsure | 10/10 | 10/10 | 10/10 | MET |
| 4. Appeal Process | 10/10 valid appeals recorded correctly | 10/10 | 10/10 | 10/10 | MET |
| 5. API Input Validation | 10/10 invalid requests return HTTP 400 | 0/10 confirmed | 0/10 confirmed | 0/10 confirmed | MISSED |

**Criterion 4 Testing Method:** The Appeal Process was tested through direct API requests using PowerShell. Each trial included 10 valid appeals. The tests verified that each appeal returned `under_review`, was linked to the correct `content_id`, preserved the original classification, and created an audit log entry.

**Evidence:** `results/appeal_criterion4_20261105_223340.json`
---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### False Positive Protection

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6632,
    "model_score": 0.7211,
    "style_score": 0.5281,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "When I was a teenager, I learned programming. That was a long time ago"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5188,
    "model_score": 0.5169,
    "style_score": 0.5233,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "In a business environment like BrightPay Solutions, comments are impor"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4409,
    "model_score": 0.3951,
    "style_score": 0.5477,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Yesterday, I went to the doctor for my anual physical evaluation. I be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5674,
    "model_score": 0.5738,
    "style_score": 0.5523,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "My background is a mix of business, operations, and compliance.  I hav"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6237,
    "model_score": 0.6025,
    "style_score": 0.6733,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "The design uses private IPv4 addressing and VLSM to give each VLAN a s"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3298,
    "model_score": 0.2625,
    "style_score": 0.4868,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "Huayruro is the name a seed from the rainforest of Peru. People who li"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.688,
    "model_score": 0.689,
    "style_score": 0.6857,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "When you are designing a network, many things come into play: the clie"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6083,
    "model_score": 0.5934,
    "style_score": 0.6431,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "In my opinion, the two most important devices in the proposed network "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4541,
    "model_score": 0.3785,
    "style_score": 0.6306,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "My daughter is a rising 8th grader and very interested in participatin"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7286,
    "model_score": 0.7749,
    "style_score": 0.6206,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "My favorite book is The Little Prince. My father used to read that boo"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6632,
    "model_score": 0.7211,
    "style_score": 0.5281,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "When I was a teenager, I learned programming. That was a long time ago"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5188,
    "model_score": 0.5169,
    "style_score": 0.5233,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "In a business environment like BrightPay Solutions, comments are impor"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4409,
    "model_score": 0.3951,
    "style_score": 0.5477,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Yesterday, I went to the doctor for my anual physical evaluation. I be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5674,
    "model_score": 0.5738,
    "style_score": 0.5523,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "My background is a mix of business, operations, and compliance.  I hav"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6237,
    "model_score": 0.6025,
    "style_score": 0.6733,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "The design uses private IPv4 addressing and VLSM to give each VLAN a s"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3298,
    "model_score": 0.2625,
    "style_score": 0.4868,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "Huayruro is the name a seed from the rainforest of Peru. People who li"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.688,
    "model_score": 0.689,
    "style_score": 0.6857,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "When you are designing a network, many things come into play: the clie"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6083,
    "model_score": 0.5934,
    "style_score": 0.6431,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "In my opinion, the two most important devices in the proposed network "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4541,
    "model_score": 0.3785,
    "style_score": 0.6306,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "My daughter is a rising 8th grader and very interested in participatin"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7286,
    "model_score": 0.7749,
    "style_score": 0.6206,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "My favorite book is The Little Prince. My father used to read that boo"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6632,
    "model_score": 0.7211,
    "style_score": 0.5281,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "When I was a teenager, I learned programming. That was a long time ago"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5188,
    "model_score": 0.5169,
    "style_score": 0.5233,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "In a business environment like BrightPay Solutions, comments are impor"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4409,
    "model_score": 0.3951,
    "style_score": 0.5477,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Yesterday, I went to the doctor for my anual physical evaluation. I be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5674,
    "model_score": 0.5738,
    "style_score": 0.5523,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "My background is a mix of business, operations, and compliance.  I hav"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6237,
    "model_score": 0.6025,
    "style_score": 0.6733,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "The design uses private IPv4 addressing and VLSM to give each VLAN a s"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3298,
    "model_score": 0.2625,
    "style_score": 0.4868,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "Huayruro is the name a seed from the rainforest of Peru. People who li"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.688,
    "model_score": 0.689,
    "style_score": 0.6857,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "When you are designing a network, many things come into play: the clie"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6083,
    "model_score": 0.5934,
    "style_score": 0.6431,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "In my opinion, the two most important devices in the proposed network "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4541,
    "model_score": 0.3785,
    "style_score": 0.6306,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "My daughter is a rising 8th grader and very interested in participatin"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7286,
    "model_score": 0.7749,
    "style_score": 0.6206,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "My favorite book is The Little Prince. My father used to read that boo"
  }
]
```

### AI-Generated Text Detection

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5973,
    "model_score": 0.6271,
    "style_score": 0.5279,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Effective project management requires a structured approach to plannin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.6122,
    "style_score": 0.532,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Cybersecurity awareness is an essential component of organizational re"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6649,
    "model_score": 0.7144,
    "style_score": 0.5494,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "Urban green spaces provide environmental, social, and public health be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4165,
    "model_score": 0.3794,
    "style_score": 0.5031,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "A well-designed customer service process balances efficiency with empa"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6513,
    "model_score": 0.6972,
    "style_score": 0.5443,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "Renewable energy adoption involves several interconnected consideratio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5916,
    "model_score": 0.5929,
    "style_score": 0.5886,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Learning a second language offers benefits that extend beyond vocabula"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4699,
    "model_score": 0.4352,
    "style_score": 0.551,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Small businesses can benefit from adopting basic data analytics practi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4755,
    "model_score": 0.4452,
    "style_score": 0.5463,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Healthcare organizations rely on accurate information exchange to coor"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4688,
    "model_score": 0.4223,
    "style_score": 0.5772,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Educational technology can expand access to learning resources when it"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2704,
    "model_score": 0.1369,
    "style_score": 0.582,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "Supply chain resilience requires organizations to anticipate disruptio"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5973,
    "model_score": 0.6271,
    "style_score": 0.5279,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Effective project management requires a structured approach to plannin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.6122,
    "style_score": 0.532,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Cybersecurity awareness is an essential component of organizational re"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6649,
    "model_score": 0.7144,
    "style_score": 0.5494,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "Urban green spaces provide environmental, social, and public health be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4165,
    "model_score": 0.3794,
    "style_score": 0.5031,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "A well-designed customer service process balances efficiency with empa"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6513,
    "model_score": 0.6972,
    "style_score": 0.5443,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "Renewable energy adoption involves several interconnected consideratio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5916,
    "model_score": 0.5929,
    "style_score": 0.5886,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Learning a second language offers benefits that extend beyond vocabula"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4699,
    "model_score": 0.4352,
    "style_score": 0.551,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Small businesses can benefit from adopting basic data analytics practi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4755,
    "model_score": 0.4452,
    "style_score": 0.5463,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Healthcare organizations rely on accurate information exchange to coor"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4688,
    "model_score": 0.4223,
    "style_score": 0.5772,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Educational technology can expand access to learning resources when it"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2704,
    "model_score": 0.1369,
    "style_score": 0.582,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "Supply chain resilience requires organizations to anticipate disruptio"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5973,
    "model_score": 0.6271,
    "style_score": 0.5279,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Effective project management requires a structured approach to plannin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.6122,
    "style_score": 0.532,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Cybersecurity awareness is an essential component of organizational re"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6649,
    "model_score": 0.7144,
    "style_score": 0.5494,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "Urban green spaces provide environmental, social, and public health be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4165,
    "model_score": 0.3794,
    "style_score": 0.5031,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "A well-designed customer service process balances efficiency with empa"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6513,
    "model_score": 0.6972,
    "style_score": 0.5443,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "Renewable energy adoption involves several interconnected consideratio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5916,
    "model_score": 0.5929,
    "style_score": 0.5886,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Learning a second language offers benefits that extend beyond vocabula"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4699,
    "model_score": 0.4352,
    "style_score": 0.551,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Small businesses can benefit from adopting basic data analytics practi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4755,
    "model_score": 0.4452,
    "style_score": 0.5463,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Healthcare organizations rely on accurate information exchange to coor"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4688,
    "model_score": 0.4223,
    "style_score": 0.5772,
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result.",
    "sent": "Educational technology can expand access to learning resources when it"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2704,
    "model_score": 0.1369,
    "style_score": 0.582,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "Supply chain resilience requires organizations to anticipate disruptio"
  }
]
```

### Signal Disagreement Handling

**Trial 1**

```json
[
  {
    "model_score": 0.9,
    "style_score": 0.1,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.85,
    "style_score": 0.15,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.8,
    "style_score": 0.2,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.95,
    "style_score": 0.05,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 1.0,
    "style_score": 0.0,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.1,
    "style_score": 0.9,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.15,
    "style_score": 0.85,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.2,
    "style_score": 0.8,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.05,
    "style_score": 0.95,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.0,
    "style_score": 1.0,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  }
]
```

**Trial 2**

```json
[
  {
    "model_score": 0.9,
    "style_score": 0.1,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.85,
    "style_score": 0.15,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.8,
    "style_score": 0.2,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.95,
    "style_score": 0.05,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 1.0,
    "style_score": 0.0,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.1,
    "style_score": 0.9,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.15,
    "style_score": 0.85,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.2,
    "style_score": 0.8,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.05,
    "style_score": 0.95,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.0,
    "style_score": 1.0,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  }
]
```

**Trial 3**

```json
[
  {
    "model_score": 0.9,
    "style_score": 0.1,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.85,
    "style_score": 0.15,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.8,
    "style_score": 0.2,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.95,
    "style_score": 0.05,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 1.0,
    "style_score": 0.0,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.1,
    "style_score": 0.9,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.15,
    "style_score": 0.85,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.2,
    "style_score": 0.8,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.05,
    "style_score": 0.95,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  },
  {
    "model_score": 0.0,
    "style_score": 1.0,
    "combined_score": 0.5,
    "guess": "unsure",
    "label": "We couldn't determine whether this text was written by a person or with AI. Writing styles vary, and this result does not indicate that you did anything wrong. You do not need to change your writing based on this result."
  }
]
```

### API Input Validation

**Trial 1**

```json
[
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "(empty text)"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"creator_id\": \"eval_invalid_02\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": null, \"creator_id\": \"eval_invalid_03\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": 123, \"creator_id\": \"eval_invalid_04\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": true, \"creator_id\": \"eval_invalid_05\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": [], \"creator_id\": \"eval_invalid_06\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": {}, \"creator_id\": \"eval_invalid_07\"}"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7098,
    "model_score": 0.7997,
    "style_score": 0.5,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "   "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.1849,
    "model_score": 0.0022,
    "style_score": 0.6111,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "{\"text\": \"A normal text without creator ID.\"}"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9983,
    "model_score": 0.9975,
    "style_score": 1.0,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 2**

```json
[
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "(empty text)"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"creator_id\": \"eval_invalid_02\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": null, \"creator_id\": \"eval_invalid_03\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": 123, \"creator_id\": \"eval_invalid_04\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": true, \"creator_id\": \"eval_invalid_05\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": [], \"creator_id\": \"eval_invalid_06\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": {}, \"creator_id\": \"eval_invalid_07\"}"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7098,
    "model_score": 0.7997,
    "style_score": 0.5,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "   "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.1849,
    "model_score": 0.0022,
    "style_score": 0.6111,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "{\"text\": \"A normal text without creator ID.\"}"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9983,
    "model_score": 0.9975,
    "style_score": 1.0,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 3**

```json
[
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "(empty text)"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"creator_id\": \"eval_invalid_02\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": null, \"creator_id\": \"eval_invalid_03\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": 123, \"creator_id\": \"eval_invalid_04\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": true, \"creator_id\": \"eval_invalid_05\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": [], \"creator_id\": \"eval_invalid_06\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": {}, \"creator_id\": \"eval_invalid_07\"}"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7098,
    "model_score": 0.7997,
    "style_score": 0.5,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "   "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.1849,
    "model_score": 0.0022,
    "style_score": 0.6111,
    "label": "This text looks more like human writing. However, no automated tool can confirm authorship with certainty.",
    "sent": "{\"text\": \"A normal text without creator ID.\"}"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9983,
    "model_score": 0.9975,
    "style_score": 1.0,
    "label": "This text has some patterns commonly found in AI-generated writing. This doesn't necessarily mean AI was used. If you wrote this yourself, you can request a review.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```
