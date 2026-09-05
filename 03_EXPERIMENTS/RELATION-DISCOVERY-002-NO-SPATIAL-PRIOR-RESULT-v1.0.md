# RELATION-DISCOVERY-002 — Blind Discovery Without Spatial Ordering

**Status:** FAIL / informative negative result

## Question

Can the blind discovery pipeline identify an extra hidden relation when the estimator is given **no spatial ordering, no distance metric, and no locality cutoff**, using only intervention-response fingerprints?

## Locked setup

- N = 40 continuous nonlinear elements.
- Periodic ring dynamics generates the data, but the estimator is blind to the ring ordering.
- Local background: self 0.48, nearest neighbours 0.10 each, second neighbours 0.035 each.
- Hidden relation: source 11 → target 31, K = +0.015.
- Intervention: +0.5 to each candidate source.
- 60 intervention times.
- Response fingerprint: 8 future time steps.
- All 1560 ordered source-target pairs are scored.
- No source/target distance information is supplied.

The estimator simply ranks the norm of each pair's 8-step response fingerprint. No generating matrix or hidden edge list is used.

## Result

The hidden pair has a substantial response:

- 11 → 31 score = **0.0129243045**

But ordinary local relations produce much larger responses. The top-ranked pairs were:

| Rank | Source → Target | Score |
|---:|---|---:|
| 1 | 17 → 16 | 0.0926634154 |
| 2 | 7 → 8 | 0.0926525438 |
| 3 | 31 → 32 | 0.0926517447 |
| 4 | 7 → 6 | 0.0926472416 |
| 5 | 22 → 23 | 0.0926432416 |
| 6 | 17 → 18 | 0.0926392416 |
| 7 | 31 → 30 | 0.0926374747 |
| 8 | 36 → 35 | 0.0926358671 |
| 9 | 30 → 31 | 0.0926330496 |
| 10 | 10 → 9 | 0.0926297487 |

**Hidden pair rank:** far below the top candidates.

Naive fingerprint-norm classification:

- ROC-AUC = **0.0577293137**
- Average precision = **0.0006410256**
- Baseline AP for one positive among 1560 pairs = **0.0006410256**

Thus the raw fingerprint norm contains essentially no useful blind localization signal for this task; it preferentially identifies ordinary local coupling.

## Attempted structure-only anomaly detection

A low-rank model was fitted to the collection of response fingerprints without using labels or spatial information. Residual anomaly scores gave:

| Rank | AUC | AP |
|---:|---:|---:|
| 1 component | 0.7947402 | 0.0031153 |
| 2 components | 0.8460552 | 0.0041494 |
| 3 components | 0.8460552 | 0.0041494 |
| 4 components | 0.7915330 | 0.0030675 |
| 5 components | 0.7261065 | 0.0023364 |
| 6 components | 0.7402181 | 0.0024630 |

This is above random ROC-AUC for some ranks, but average precision remains very low because the positive class is 1/1560 and the hidden relation is not the strongest anomaly.

## Interpretation

This is an important negative result.

When spatial ordering is removed, the problem changes qualitatively. A response fingerprint by itself does not tell us whether a strong source-target response is an ordinary local relation or an additional nonlocal relation. The hidden 11 → 31 relation is weaker than the ordinary local couplings and is therefore buried among them.

The previous successful blind experiment used observable spatial ordering plus a distant-target constraint. Removing that prior makes the task substantially harder and defeats the simple fingerprint detector.

## What this establishes

1. **Relation is not recoverable from response magnitude alone.**
2. Observable geometry/order can provide information that is not contained in a scalar response score.
3. A successful relation detector must separate background structure from candidate excess structure.
4. Blind discovery without an assumed geometry is possible only if the response representation contains enough structure to infer the background and the anomaly simultaneously; this experiment did not achieve that.

## What it does NOT establish

- It does not show that blind discovery without geometry is impossible in principle.
- It does not refute the operational definition of relation as reproducible response structure.
- It does not establish a physical ontology of relations.

## Next test

Construct the estimator around **response equivalence classes** rather than pair magnitude:

1. cluster source-response fingerprints;
2. learn the dominant background propagation operator from the ensemble itself;
3. detect excess residual propagation;
4. predict source and target from that residual;
5. perform an independent confirmation intervention.

The key question becomes: **can geometry itself be reconstructed from response structure, rather than assumed?**
