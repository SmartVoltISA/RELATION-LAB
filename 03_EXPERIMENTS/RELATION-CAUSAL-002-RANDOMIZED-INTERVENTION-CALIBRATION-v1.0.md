# RELATION-CAUSAL-002 — Randomized Source/Target Intervention Calibration v1.0

## Status
**EXECUTED / CONTROLLED SYNTHETIC RESULT**

## Question
Can intervention response recover direct relation strength when source and target are randomized, without using passive correlation?

## Setup
- N = 12 state variables.
- Sparse directed linear dynamical system.
- 144 ordered source→target pairs tested.
- Intervention magnitudes δ = 0.5, 1.0, 2.0.
- Direct response estimated as normalized lag-1 target response divided by δ.
- Ground truth is the generating transition coefficient.

## Numerical result
The normalized intervention estimator recovered the direct coefficient for all tested pairs.

| Metric | Result |
|---|---:|
| Ordered pairs | 144 |
| Intervention magnitudes | 0.5, 1.0, 2.0 |
| ROC-AUC | **1.000000** |
| Average precision | **1.000000** |

Representative recovered coefficients:

| Source | Target | True coefficient | Estimated intervention coefficient |
|---:|---:|---:|---:|
| 0 | 1 | +0.12 | +0.12 |
| 0 | 2 | −0.10 | −0.10 |
| 2 | 5 | +0.12 | +0.12 |
| 4 | 1 | −0.10 | −0.10 |
| 7 | 10 | −0.10 | −0.10 |
| 9 | 3 | +0.08 | +0.08 |
| 10 | 11 | −0.10 | −0.10 |

## Interpretation
This is a calibration/control experiment. In a correctly specified linear system, the first-lag controlled response directly exposes the local transition coefficient. Normalizing by δ also verifies linear scaling over the tested intervention range.

The result strengthens the operational definition:

> A candidate relation can be measured as a reproducible state-transition response under controlled intervention.

## Critical limitation
This experiment is deliberately clean. The generating dynamics are linear, the intervention is instantaneous, and the direct coefficient is the local causal effect by construction. Therefore ROC-AUC=1 does **not** establish universal relation recoverability.

The next experiment must be harder: nonlinear dynamics, correlated hidden variables, indirect paths, unknown background coupling, and held-out source/target pairs. The estimator must then distinguish direct relation from mediated response without access to the generating matrix.

## Decision
**PASS — calibration/control only.**

Do not upgrade the ontological claim. The experiment validates the measurement mechanism under controlled conditions and defines the next falsification target.
