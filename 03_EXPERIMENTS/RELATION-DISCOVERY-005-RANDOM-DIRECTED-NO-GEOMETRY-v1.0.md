# RELATION-DISCOVERY-005 — Random Directed Background Without Geometry

**Status:** PASS for directed relation recovery; finite detection regime

## Question

Can a relation be recovered from intervention-response data when the generating system has **no spatial geometry at all**?

The test removes the periodic ring and all notions of distance. Forty elements are connected by a random sparse directed background. One additional hidden directed relation is injected. The estimator receives only intervention-response data.

## Locked setup

- N = 40 elements.
- No spatial coordinates, ordering, distance, neighbourhoods, or locality assumptions.
- Random directed background: 120 ordered edges.
- Background edge weights: approximately ±0.008 to ±0.030.
- Hidden relation: **17 → 29**, K = +0.080.
- Nonlinear dynamics: `x[t+1] = tanh(0.62*x[t] + A*x[t] + noise)`.
- Noise scale = 0.020.
- Intervention amplitude = +0.5.
- Training interventions: 160 source interventions.
- Confirmation interventions: 50 fresh interventions.
- Response horizon for confirmation: 8 steps.
- All 1560 ordered non-self pairs are evaluated.
- Generating matrix A and hidden edge are not supplied to the estimator.

## Estimator

For every candidate source, a paired intervention is performed using identical future noise in the control and perturbed trajectories. The mean one-step normalized target response estimates the directed response operator.

The estimator then ranks all ordered pairs by absolute directed response magnitude. No geometry is used because none exists.

For confirmation, the candidate pair is frozen. The learned response operator is propagated forward for 8 steps to produce a predicted response fingerprint. A new set of interventions with independent noise is then used to test that prediction.

## Main result

| Quantity | Result |
|---|---:|
| Hidden relation | **17 → 29** |
| Estimated coefficient, seed 20260905 | **0.0799191** |
| True coefficient | **0.0800000** |
| Hidden-pair rank | **1 / 1560** |
| ROC-AUC | **1.000000** |
| Average Precision | **1.000000** |
| Direction accuracy | **1.000** |
| Top-1 recovery | **1.000** |

## Multi-seed verification

| Seed | AUC | AP | Rank | Estimated K | Direction |
|---:|---:|---:|---:|---:|---|
| 1 | 1.000000 | 1.000000 | 1 | 0.079907 | 17 → 29 |
| 2 | 1.000000 | 1.000000 | 1 | 0.079904 | 17 → 29 |
| 3 | 1.000000 | 1.000000 | 1 | 0.079914 | 17 → 29 |
| 4 | 1.000000 | 1.000000 | 1 | 0.079886 | 17 → 29 |
| 5 | 1.000000 | 1.000000 | 1 | 0.079920 | 17 → 29 |
| 20260905 | 1.000000 | 1.000000 | 1 | 0.079919 | 17 → 29 |

## Independent prediction test — seed 20260905

The source-target pair was frozen after training. The following 8-step fingerprint was predicted from the learned directed response operator and then measured using 50 fresh interventions.

| Lag | Predicted | Confirmed | Difference |
|---:|---:|---:|---:|
| 1 | 0.07991911 | 0.07987883 | -0.00004028 |
| 2 | 0.09909969 | 0.09745340 | -0.00164629 |
| 3 | 0.09216271 | 0.08972567 | -0.00243704 |
| 4 | 0.07618782 | 0.07370361 | -0.00248421 |
| 5 | 0.05904551 | 0.05687311 | -0.00217240 |
| 6 | 0.04392978 | 0.04217970 | -0.00175008 |
| 7 | 0.03177578 | 0.03043789 | -0.00133789 |
| 8 | 0.02251531 | 0.02152839 | -0.00098692 |

- Fingerprint correlation: **0.99959896**
- RMSE: **0.00178074**

## Null check

The same experiment was repeated with the hidden relation coefficient set to K = 0 while retaining the nominal pair label 17 → 29.

| Quantity | K = 0 null |
|---|---:|
| Mean AUC across 6 seeds | **0.46151** |
| Mean AP | **0.000640** |
| Baseline AP | **1/1560 = 0.000641** |
| Top-1 nominal hidden pair | **0 / 6** |

The null therefore does not systematically recover the absent relation.

## Detection-boundary sweep

| K | Mean AUC | Mean AP | Mean rank | Top-1 rate |
|---:|---:|---:|---:|---:|
| 0.000 | 0.4615 | 0.000640 | 121.0 | 0/6 |
| 0.020 | 0.9754 | 0.0255 | 39.3 | 0/6 |
| 0.025 | 0.9870 | 0.0481 | 21.3 | 0/6 |
| 0.030 | 0.9999 | 0.9167 | 1.17 | 5/6 |
| 0.035 | 1.0000 | 1.0000 | 1.0 | 6/6 |
| 0.040 | 1.0000 | 1.0000 | 1.0 | 6/6 |
| 0.060 | 1.0000 | 1.0000 | 1.0 | 6/6 |
| 0.080 | 1.0000 | 1.0000 | 1.0 | 6/6 |

## Interpretation

This is the first test in the sequence in which the **data-generating system itself has no geometry**. The successful recovery therefore cannot be attributed to a reconstructed distance or locality prior.

The result supports a narrower statement:

> A directed relation can be operationally recovered from intervention-response data without requiring a spatial geometry.

The recovered object is a directed component of the response operator.

The experiment also shows an important limit. When K is reduced toward the scale of ordinary background coefficients, reliable identification degrades. At K = 0.020 the relation is statistically distinguishable in aggregate (AUC ≈ 0.975) but is not top-ranked; at K = 0.030 it is nearly always top-ranked; at K ≥ 0.035 it is top-ranked in all six seeds.

Thus the method has a finite signal-to-background detection regime rather than unlimited sensitivity.

## What this establishes

1. Spatial geometry is **not necessary** for operational recovery of a directed relation in this class of dynamical systems.
2. Direction can be inferred from intervention response.
3. A relation can be represented as a component of a learned directed response operator.
4. A frozen prediction can be independently confirmed with a new intervention series.
5. The result survives six independent random seeds.

## What this does NOT establish

- It does not prove that all physical relations are directed causal coefficients.
- It does not prove that physical space is emergent from relations in general.
- It does not establish universal detection thresholds.
- The background is synthetic and deliberately sparse.
- The estimator uses controlled interventions; passive observation alone was not tested here.

## Current conclusion

The evidence now supports a stronger separation:

**Geometry is optional for relation recovery.**

A graph is therefore useful as a representation, but it is not required as the physical or mathematical substrate of the operational relation.

The next decisive test is to remove the special distinction between “background edge” and “hidden edge”: draw all relations from the same distribution and ask whether the system can discover a reproducible causal relation at all, rather than an artificially stronger injected edge. That test addresses whether **relation itself**, rather than anomaly detection, is the fundamental observable.
