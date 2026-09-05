# REL-EXP-001 — Time-varying relation recovery

Date: 2026-09-05
Status: EXECUTED — SYNTHETIC CONTROLLED EXPERIMENT

## Question

Can a changing relation `K_AB(t)` be recovered from observed states without exposing the true coupling to the estimator?

## Generative system

A and B are simulated as stochastic state variables. B depends on its own previous state and on A with a piecewise constant coupling. The estimator receives only the generated state series.

True coupling:

| Window | K_AB |
|---|---:|
| 0–1000 | 0.000 |
| 1000–2000 | +0.800 |
| 2000–3000 | +0.200 |
| 3000–4000 | 0.000 |
| 4000–5000 | −0.700 |

## Recovery

| Window | True K_AB | Estimated K_AB | Absolute error |
|---|---:|---:|---:|
| 0–1000 | 0.000 | −0.016 | 0.016 |
| 1000–2000 | +0.800 | +0.807 | 0.007 |
| 2000–3000 | +0.200 | +0.187 | 0.013 |
| 3000–4000 | 0.000 | +0.016 | 0.016 |
| 4000–5000 | −0.700 | −0.631 | 0.069 |

Mean absolute error: 0.024.

## Interpretation

The estimator recovered presence, approximate magnitude, disappearance and sign reversal of the changing relation.

## Control

After destroying temporal alignment by shuffling B, estimated coefficients were approximately zero across all windows:

| Window | Shuffled estimate |
|---|---:|
| 0–1000 | +0.007 |
| 1000–2000 | −0.032 |
| 2000–3000 | +0.010 |
| 3000–4000 | −0.007 |
| 4000–5000 | −0.045 |

## Conclusion

Within this synthetic model, a time-varying relation can be recovered from observed state transitions. This does not establish a physical relation in nature and does not validate the estimator outside the tested model class.
