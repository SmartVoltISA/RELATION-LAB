# RELATION-DISCOVERY-001 — Blind Find → Predict → Confirm

**Status:** PASS (synthetic continuous nonlinear medium; finite detection regime)

## Question

Can an algorithm discover a candidate relation without being given the generating interaction matrix or hidden edge list, first identify the source, then infer the target region from the full spatiotemporal response, and finally confirm the prediction with an independent intervention?

## Locked model

- N = 40 elements on a periodic ring.
- T = 5000 time steps.
- Local background coupling: nearest neighbours 0.10 each; second neighbours 0.035 each.
- Nonlinear update: `x[t+1] = tanh(0.35*x[t] + 0.48*x[t] + local + hidden + 0.18*0.12*noise)`.
- Hidden relation: source 11 → target 31, K = +0.015.
- Intervention: +0.5 to one candidate source element.
- Response horizon: 8 steps.
- Discovery: 40 intervention times, all 40 candidate sources tested.
- Target candidates were not supplied; target was selected from the resulting spatial response fingerprint outside a local radius of 8.
- Confirmation: 30 new intervention times, independent noise realizations.
- The discovery and confirmation time sets are disjoint.

The algorithm is blind to the generating matrix and hidden edge list. It does know the element labels and periodic spatial ordering because those are observable properties of the simulated medium.

## Discovery result

For each candidate source, the score was the maximum absolute cumulative response over target elements at circular distance >= 9 from the source. This suppresses the immediate local background and searches for a distant coherent response.

| Rank | Candidate source | Best distant target | Score |
|---:|---:|---:|---:|
| 1 | 11 | 31 | 0.0456801739 |
| 2 | 12 | 31 | 0.0079773813 |
| 3 | 10 | 31 | 0.0079545464 |
| 4 | 13 | 31 | 0.0034314803 |
| 5 | 9 | 31 | 0.0034107060 |
| 6 | 8 | 31 | 0.0007117139 |
| 7 | 14 | 31 | 0.0006950561 |
| 8 | 15 | 31 | 0.0001965511 |

**Source rank:** 1/40.

**Source score / runner-up:** 5.7262117×.

**Predicted target:** 31, rank 1 among the distant target candidates for the discovered source 11.

## Predicted response fingerprint

For source 11 and predicted target 31, the discovery-phase mean signed response was:

| Lag | Predicted response |
|---:|---:|
| 1 | 0.00550315 |
| 2 | 0.00741570 |
| 3 | 0.00754042 |
| 4 | 0.00684985 |
| 5 | 0.00591251 |
| 6 | 0.00496575 |
| 7 | 0.00411382 |
| 8 | 0.00337899 |

## Independent confirmation

A fresh intervention series was run at 30 new times, using independent noise. The previously predicted source-target pair (11 → 31) was not re-selected during confirmation; it was tested as a locked prediction.

| Lag | Predicted | Confirmed |
|---:|---:|---:|
| 1 | 0.00550315 | 0.00552308 |
| 2 | 0.00741570 | 0.00745731 |
| 3 | 0.00754042 | 0.00761179 |
| 4 | 0.00684985 | 0.00692271 |
| 5 | 0.00591251 | 0.00599896 |
| 6 | 0.00496575 | 0.00505097 |
| 7 | 0.00411382 | 0.00419734 |
| 8 | 0.00337899 | 0.00344509 |

- Fingerprint correlation: **0.9998844641**
- RMSE: **0.0000694741**
- Least-squares scale factor (confirmed / predicted): **1.0106740**

## Matched causal null

Using the same source 11 and target 31, but setting the hidden relation coefficient K = 0 during the response calculation, the distant target response through lag 8 was exactly zero in this finite-propagation setup (the local background cannot reach distance 20 within 8 steps).

- Confirmed K = +0.015: response norm = **0.0168215724**
- Matched K = 0 null: response norm = **0.0000000000**

## Decision

**PASS for the locked synthetic question.**

The procedure successfully executed the requested chain:

`find source → infer target → predict response fingerprint → independent intervention → confirm fingerprint`.

The important result is not merely that 11 → 31 was recoverable. The target and the time profile were inferred before the confirmation intervention, and the independent confirmation reproduced the predicted temporal response with correlation 0.999884.

## What this establishes

1. In this model, a relation can be operationally discovered from intervention-response structure without access to the generating interaction matrix.
2. A full temporal fingerprint is substantially richer than a one-step scalar response.
3. A discovered relation can be treated as a falsifiable prediction: the predicted source, target, sign, and response profile can be frozen and then tested independently.
4. This supports the working operational definition: **relation = reproducible conditional response structure under controlled intervention**.

## What it does NOT establish

- It does not prove that every physical system admits this discovery procedure.
- It does not prove a universal ontology of relations.
- K = 0.015 is not a universal physical detection threshold; it is a parameter of this experiment.
- The experiment is synthetic and uses a known spatial ordering and a deliberately designed local background.

## Next falsification target

Repeat the same blind pipeline while progressively removing prior structure available to the estimator:

1. hide spatial ordering;
2. allow multiple hidden relations;
3. vary sign and temporal memory;
4. add common-cause and mediated pathways;
5. sweep K through and below the previously observed detection boundary;
6. require the algorithm to discover source and target without any distance/locality cutoff chosen from the hidden model.

The strongest next test is therefore **blind self-discovery under unknown locality**, followed by independent confirmation.

---

**Reproducibility:** random seeds used for the medium/intervention streams: 20260905, 777, 888. Exact numerical values above are the values produced by the executed run.
