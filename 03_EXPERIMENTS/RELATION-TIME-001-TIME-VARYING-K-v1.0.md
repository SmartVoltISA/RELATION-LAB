# RELATION-TIME-001 — Time-varying relation recovery

**Status:** EXECUTED / VERIFIED PILOT
**Date:** 2026-09-05

## Question
Can a time-varying directional relation K_AB(t) be recovered from observations when the coupling changes magnitude and sign over time?

## Model
Two continuous state variables:

- A[t+1] = 0.55 A[t] + ε_A
- B[t+1] = 0.55 B[t] + c[t] A[t] + ε_B
- ε_A, ε_B ~ N(0, 0.25²)

The true directional relation is K_BA(t)=c[t].

Segments:

| Time | True K_BA |
|---:|---:|
| 0–999 | 0.00 |
| 1000–1999 | +0.80 |
| 2000–2999 | +0.20 |
| 3000–3999 | 0.00 |
| 4000–4998 | −0.70 |

Random seed: 20260905.

## Recovery method
Non-overlapping windows of 200 transitions. In each window fit:

B[t+1] = β_A A[t] + β_B B[t] + residual

with ridge α=1e−8 and no intercept. β_A is the recovered local estimate of K_BA.

## Numerical result

| Window | True K | Estimated β_A |
|---:|---:|---:|
| 0–199 | 0.00 | −0.0361 |
| 200–399 | 0.00 | +0.0351 |
| 400–599 | 0.00 | −0.0257 |
| 600–799 | 0.00 | −0.0187 |
| 800–999 | 0.00 | −0.0161 |
| 1000–1199 | +0.80 | +0.7214 |
| 1200–1399 | +0.80 | +0.8104 |
| 1400–1599 | +0.80 | +0.7497 |
| 1600–1799 | +0.80 | +0.8825 |
| 1800–1999 | +0.80 | +0.8111 |
| 2000–2199 | +0.20 | +0.2768 |
| 2200–2399 | +0.20 | +0.2200 |
| 2400–2599 | +0.20 | +0.2047 |
| 2600–2799 | +0.20 | +0.2636 |
| 2800–2999 | +0.20 | +0.1874 |
| 3000–3199 | 0.00 | +0.0497 |
| 3200–3399 | 0.00 | −0.0656 |
| 3400–3599 | 0.00 | +0.0385 |
| 3600–3799 | 0.00 | +0.0175 |
| 3800–3999 | 0.00 | +0.1374 |
| 4000–4199 | −0.70 | −0.7905 |
| 4200–4399 | −0.70 | −0.5605 |
| 4400–4599 | −0.70 | −0.7182 |
| 4600–4799 | −0.70 | −0.7241 |

## Aggregate metrics

| Metric | Result |
|---|---:|
| Pearson correlation(true, estimate) | 0.991959 |
| RMSE | 0.059889 |
| Sign agreement | 58.33% |
| ROC-AUC for active relation | 1.000000 |
| Average precision for active relation | 1.000000 |

For the binary active-relation test, active means |K| > 0.10. Sign agreement is low only because exact zero windows have no meaningful sign; the magnitude/time profile is the stronger test here.

## Negative control
A was independently time-shuffled before the same windowed regression, destroying temporal correspondence with B while preserving the marginal A distribution.

| Metric | Original | Time-shuffled control |
|---|---:|---:|
| ROC-AUC | 1.000000 | 0.414286 |
| Average precision | 1.000000 | 0.592054 |
| Correlation(true, estimate) | 0.991959 | −0.027637 |
| RMSE | 0.059889 | 0.475303 |

## Interpretation
The experiment successfully recovers a changing directional relation from continuous observations in this controlled model. It recovers both **magnitude** and **sign** of the coupling, including the transition from 0 → +0.8 → +0.2 → 0 → −0.7.

The result is evidence for **recoverability in the specified dynamical model**, not evidence that every physical relation is a scalar K_ij, nor that K_ij(t) is ontologically fundamental.

## Limits
1. The true model form is known and correctly specified.
2. There are only two variables.
3. Coupling acts with one-step delay.
4. Noise is Gaussian and stationary.
5. Windowing introduces temporal resolution limits.
6. This is a synthetic dynamical experiment, not a physical measurement.

## Next decisive test
Move from the clean two-variable system to a continuous spatial field with many correlated elements and a hidden time-varying local coupling. Recover K_ij(t) without revealing the target edge to the estimator, and compare against spatially shuffled and temporally shuffled controls.
