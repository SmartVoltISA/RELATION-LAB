# REL-EXP-002 — Continuous-field relation recovery

Date: 2026-09-05
Status: EXECUTED — SYNTHETIC EXPERIMENT

## Question

Can a relation structure be recovered when the system is represented by a continuous-like field sampled at many spatial elements?

## Model

A 40-element field was simulated with local and second-neighbor dynamical coupling. The estimator reconstructed a Jacobian-like influence matrix from state transitions using regularized regression.

## Recovery quality

| Metric | Value |
|---|---:|
| Elements | 40 |
| True relation structure | local + second-neighbor |
| ROC-AUC | 0.7548 |
| Average Precision | 0.4580 |
| Time-shuffled ROC-AUC | 0.5418 |
| Time-shuffled Average Precision | 0.1123 |

## Interpretation

The real temporal structure carried substantially more information about relation than the shuffled control, but recovery was imperfect. This is an important negative/limiting result: correlated continuous states make relation reconstruction substantially harder than the simple two-variable case.

## Conclusion

The experiment supports feasibility of relation recovery in a continuous-like dynamical system, while demonstrating that the estimator is not yet sufficient as a general relation detector.
