# AI-use policy

**Status:** decided 9 November 2026 ([decision log](../docs/decisions.md)).

Required work **never depends** on any AI tool or paid API. AI assistance is allowed where it supports learning and can be verified.

| Context | Allowed? | Conditions |
|---|---|---|
| **Labs and project** | **Yes**: code completion, explanation, debugging, including Colab's built-in assistant where your account offers it | 1. Complete the **AI-use log** in every submission. 2. You must be able to **explain any submitted cell**; this is checked in the random-member project Q&A and by spot checks. 3. Do not paste non-public data or other students' work into AI tools. 4. Fabricated outputs, results or citations are academic misconduct. |
| **AI-audit tasks** (Lab 1, graded lab G1, Lab 6, graded lab G5) | **Required** | You critique instructor-supplied AI-generated code that contains planted errors (leakage, sentinel values, a wrong loss). The skill being taught is verification, not prompting. |
| **Midterm and final examinations** | **No** | In person, with no AI tools and no internet. |

## The AI-use log

Every lab ends with this table. The project uses the same columns in `ai-use.md`.

| Tool | What you asked or used it for | What you accepted or changed | How you verified it |
|---|---|---|---|
| e.g. Colab AI | explain `np.linalg.svd` output shapes | used the explanation, wrote my own code | the self-check passed; compared with lecture §5.5 |

**What counts as verification:** a passing test or self-check, a hand calculation, comparison with library documentation, or reproducing a known result. "It looked right" is not verification.

Undisclosed or unverifiable use is handled under the faculty's existing academic-integrity procedures, which this policy does not restate.
