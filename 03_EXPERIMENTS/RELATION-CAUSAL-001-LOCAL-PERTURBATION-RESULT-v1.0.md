# RELATION-CAUSAL-001 — Local Perturbation Result v1.0

## Status
**EXECUTED / NUMERICAL RESULT / NEGATIVE-AND-POSITIVE MIXED RESULT**

## Question
Can a controlled local perturbation recover a time-varying relation in a many-element continuous analogue-like medium more cleanly than passive observation?

## Model
N = 40 elements on a periodic 1D domain.

Update:

`x[t+1] = x[t] + 0.035 * (-x[t] + drive) + 0.04 * noise`

`drive = 0.50*x + 0.10*(nearest neighbours) + 0.035*(second neighbours) + K(t)*x[10] into target 11`

Hidden time-varying relation 10 -> 11:

| Segment | K |
|---:|---:|
| 0–999 | 0.00 |
| 1000–1999 | +0.18 |
| 2000–2999 | +0.05 |
| 3000–3999 | 0.00 |
| 4000–4999 | −0.16 |

A unit intervention was applied to source 10. Control and intervention trajectories started from the same state and used identical future noise, so the difference isolates the intervention response.

## Main response
Because source 10 is also a nearest neighbour of target 11, even K=0 produces a baseline direct response. Therefore the hidden relation must be identified from the **increment above the K=0 baseline**, not from raw target response alone.

At lag 1 the baseline response is 0.003500. The predicted incremental contribution of K is `0.035*K`, giving:

| K | Observed lag-1 response | K contribution above baseline | Expected 0.035*K |
|---:|---:|---:|---:|
| 0.00 | +0.003500 | +0.000000 | +0.000000 |
| +0.18 | +0.009800 | +0.006300 | +0.006300 |
| +0.05 | +0.005250 | +0.001750 | +0.001750 |
| −0.16 | −0.002100 | −0.005600 | −0.005600 |

This is an exact recovery at the first permitted lag for this specified linear intervention model.

## Response over time
| K | Lag | Target response ΔX11 |
|---:|---:|---:|
| 0.00 | 1 | +0.003500 |
| 0.00 | 2 | +0.006886 |
| 0.00 | 5 | +0.016390 |
| 0.00 | 10 | +0.030210 |
| 0.00 | 20 | +0.051376 |
| 0.00 | 50 | +0.079651 |
| +0.18 | 1 | +0.009800 |
| +0.18 | 2 | +0.019266 |
| +0.18 | 5 | +0.045747 |
| +0.18 | 10 | +0.084006 |
| +0.18 | 20 | +0.141884 |
| +0.18 | 50 | +0.216610 |
| +0.05 | 1 | +0.005250 |
| +0.05 | 2 | +0.010325 |
| +0.05 | 5 | +0.024544 |
| +0.05 | 10 | +0.045151 |
| +0.05 | 20 | +0.076493 |
| +0.05 | 50 | +0.117447 |
| −0.16 | 1 | −0.002100 |
| −0.16 | 2 | −0.004118 |
| −0.16 | 5 | −0.009703 |
| −0.16 | 10 | −0.017584 |
| −0.16 | 20 | −0.028877 |
| −0.16 | 50 | −0.040013 |

## Source permutation control
At K=+0.18, lag 10, the target response was measured after intervening on alternative source indices.

| Intervention source | Mean ΔX11 |
|---:|---:|
| 0 | 0.000000 |
| 5 | 0.000000 |
| 10 | +0.084006 |
| 15 | +0.000063 |
| 20 | 0.000000 |
| 30 | 0.000000 |
| 35 | 0.000000 |

Only the designated source 10 produces the large target response. The tiny response from source 15 is consistent with a very weak longer-path/background effect at this lag.

## Important methodological finding
The experiment demonstrates why a raw pairwise response is insufficient for identifying a specific relation in a many-element medium.

`source 10 -> target 11` already has a structural nearest-neighbour pathway when the hidden K is zero. The controlled perturbation therefore measures:

`observed response = baseline structural response + hidden relation contribution + indirect effects`

The hidden relation is recoverable here because the K=0 baseline is known and the intervention response changes exactly with K.

## What this establishes
1. A relation can be operationalized as a reproducible response under a controlled intervention.
2. A time-varying relation can be recovered from the change in intervention response, even when a background coupling is already present.
3. Sign and magnitude of the hidden relation are recovered exactly at the first dynamically permitted lag in this model.
4. Source permutation provides a strong negative control.
5. The result supports **causal recoverability in the specified model**, not an ontological claim that K is a fundamental physical relation.

## What this does NOT establish
- It does not show that every continuous physical system admits such recovery.
- It does not prove that a physical universe has a primitive relation field K.
- It does not identify electrons, particles, fields, or fundamental ontology.
- It does not show that passive observation alone is sufficient.

## Relation-LAB consequence
The earlier passive many-element Jacobian experiment was unstable at short windows. This result changes the next methodological step: **local intervention/response should be treated as the primary operational probe, while passive correlation/Jacobian estimation remains a secondary observational method.**

## Reproducibility
- Seeds: 10 independent initial states.
- Paired control/intervention trajectories used identical future noise.
- Intervention magnitude: +1.0 at source 10.
- Lags: 1, 2, 5, 10, 20, 50.
- Source permutation control executed.

## Decision
**PASS for the locked causal-probe question in the specified model.**

**Next test:** remove knowledge of the hidden K=0 baseline and attempt to recover direct relation strength from intervention responses alone while separating direct and indirect pathways. Include ±δ scaling and a larger randomized source/target set.
