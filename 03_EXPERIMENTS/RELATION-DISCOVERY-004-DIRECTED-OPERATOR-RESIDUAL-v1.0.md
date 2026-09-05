# RELATION-DISCOVERY-004 — Directed Response Operator + Residual

**Status:** PASS (synthetic continuous nonlinear medium; finite detection regime)

## Question

Can the hidden relation be recovered by first reconstructing the ordinary directed propagation structure from intervention responses, without using the true geometry, and then identifying the irreducible residual?

## Locked setup

- N = 40 continuous nonlinear elements.
- Periodic-ring dynamics generates the data, but this geometry is not supplied to the estimator.
- Background operator: self 0.48; nearest neighbours 0.10 each; second neighbours 0.035 each.
- Hidden relation: physical source 11 → physical target 31, K = +0.015.
- T = 5000.
- Intervention amplitude = +0.5.
- 1800 intervention source/response observations (45 times × 40 sources).
- Response horizon = 8 steps.
- Estimator receives only intervention-response fingerprints.
- No generating matrix, edge list, spatial ordering, distance metric, or locality cutoff is supplied.

## Method

1. For every source, estimate its mean one-step response to every target.
2. Construct a source-response similarity matrix from these directed response profiles.
3. Recover a latent cyclic ordering by greedy seriation of response-profile similarity. This is an estimator-generated structure, not the true ordering.
4. Estimate the expected background response for each source-target pair from other pairs at the same recovered structural distance.
5. Score each pair by the absolute residual between observed one-step response and its background expectation.
6. Rank all 1560 ordered pairs.

The true hidden edge list is never used by the estimator.

## Main result

The recovered latent ordering placed the true source and target at structural distance 20, matching the true antipodal distance without being given the physical labels.

| Quantity | Result |
|---|---:|
| Hidden source → target | **11 → 31** |
| Recovered structural distance | **20** |
| True structural distance | **20** |
| Hidden-pair residual score | **0.0147410462** |
| Hidden-pair rank | **1 / 1560** |
| ROC-AUC | **1.000000** |
| Average Precision | **1.000000** |

## Multi-seed verification

| Seed | AUC | AP | Top-ranked pair | Recovered distance |
|---:|---:|---:|---|---:|
| 1 | 1.000000 | 1.000000 | 11 → 31 | 20 |
| 2 | 1.000000 | 1.000000 | 11 → 31 | 20 |
| 3 | 1.000000 | 1.000000 | 11 → 31 | 20 |
| 4 | 1.000000 | 1.000000 | 11 → 31 | 20 |
| 5 | 1.000000 | 1.000000 | 11 → 31 | 20 |
| 20260905 | 1.000000 | 1.000000 | 11 → 31 | 20 |

## Null / detection boundary check

With the hidden coefficient set to K = 0, there is no true positive relation. The same detector produced ROC-AUC = 0.448686 against the nominal hidden-pair label and ranked an ordinary local pair first, indicating no systematic recovery of the absent relation.

A single-seed signal sweep gave:

| K | AUC | AP | Top-ranked pair |
|---:|---:|---:|---|
| 0.000 | 0.4487 | 0.000641 | 29 → 28 |
| 0.005 | 1.0000 | 1.0000 | 11 → 31 |
| 0.010 | 1.0000 | 1.0000 | 11 → 31 |
| 0.015 | 1.0000 | 1.0000 | 11 → 31 |
| 0.020 | 1.0000 | 1.0000 | 11 → 31 |

The K = 0 AUC is not interpreted as a classification performance number because there is no actual positive; it is included only as a null sanity check.

## Comparison with previous failures

- Raw response magnitude without geometry failed because strong ordinary local relations dominated.
- Low-rank anomaly detection found some atypical structure but did not reliably isolate the single hidden relation.
- The present estimator first reconstructs a latent directed background structure from the response ensemble and then searches for excess response relative to that structure.

## Interpretation

This experiment supports a stronger operational statement than the previous discovery attempts:

> A relation can appear as an **irreducible residual of a learned directed response operator**.

The important object is therefore not a graph edge and not simply a large response. It is a reproducible source-target response that remains after the regular propagation structure has been estimated from the system itself.

## What this establishes

1. In this locked synthetic model, latent structural organization can be recovered from intervention-response profiles without supplying the true geometry.
2. Once that background is reconstructed, the additional hidden relation can be isolated as a residual.
3. The same source-target pair was recovered across six independent seeds.
4. The method does not depend on a pre-supplied locality cutoff for the final relation score.

## What this does NOT establish

- It does not prove that geometry can always be reconstructed from responses.
- It does not prove a universal physical ontology of relations.
- K = 0.005 is not a universal physical detection threshold.
- The greedy seriation method is still an algorithmic prior and may fail on other classes of dynamics.
- The experiment is synthetic.

## Next falsification target

Remove the periodic-ring prior from the **data-generating system itself** and replace it with a random sparse directed background having no geometric ordering. Then inject one additional hidden relation and test whether the same background-plus-residual procedure can recover it without relying on any geometry at all.

The decisive question becomes:

**Can relation be recovered as an irreducible component of a learned response operator even when the underlying system has no predefined spatial geometry?**
