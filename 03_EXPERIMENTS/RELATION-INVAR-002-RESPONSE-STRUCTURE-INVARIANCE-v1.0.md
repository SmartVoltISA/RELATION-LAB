# RELATION-INVAR-002 — Response-Structure Invariance

**Status:** EXECUTED / VERIFIED
**Date:** 2026-09-05
**Purpose:** test whether an operational relation defined by controlled response preserves its source→target structure under element-preserving coordinate changes, spatial permutation, and temporal coarse-graining.

## 1. Locked question

If relation is operationally represented by a reproducible intervention response, which parts are invariant under a change of representation or observational scale?

## 2. Model

N = 10 nonlinear dynamical elements.

x[t+1] = tanh(A x[t] + 0.35 x[t] + 0.12 noise)

Hidden direct relations:

| source | target | coefficient |
|---:|---:|---:|
| 0 | 1 | +0.55 |
| 1 | 2 | +0.50 |
| 3 | 1 | +0.35 |
| 3 | 2 | +0.25 |
| 4 | 5 | -0.45 |
| 5 | 6 | +0.40 |
| 6 | 7 | +0.30 |
| 8 | 9 | +0.50 |

Seed = 11 for the trajectory; 120 intervention times were selected from t >= 1000.

For each ordered source-target pair, intervention was x_i -> x_i + delta and the one-step response of the target was measured. Direct-edge labels were evaluated with ROC-AUC and average precision.

## 3. Element-preserving coordinate transforms

The same physical state was represented as:

1. X_i = x_i
2. Y_i = sinh(x_i)
3. Z_i = x_i^3 + x_i

These transforms are invertible and preserve the identity of each element; they change numerical response magnitude but not the element decomposition.

### Results

| representation | ROC-AUC | AP | corr(response, true coefficient) |
|---|---:|---:|---:|
| X | 1.000000 | 1.000000 | 0.999995 |
| sinh(X) | 1.000000 | 1.000000 | 0.999999 |
| X^3+X | 1.000000 | 1.000000 | 0.999987 |

**Result: PASS.** Direct source→target support is invariant in this controlled model under element-preserving invertible nonlinear reparameterization.

## 4. Spatial / index permutation

A random permutation of the ten element labels was applied. The transformed dynamics used the correspondingly permuted interaction matrix and states. Direct-edge labels were permuted with the elements.

Permutation used:

[9, 5, 4, 7, 3, 0, 1, 8, 6, 2]

### Result

| test | ROC-AUC | AP |
|---|---:|---:|
| permuted element coordinates | 1.000000 | 1.000000 |

**Result: PASS.** Relation structure follows the elements, not their numerical labels/order.

## 5. Temporal coarse-graining

The trajectory was sampled through q-step dynamics and the same intervention response was measured after q physical update steps. The target labels remained the original direct one-step edges.

| q (physical update steps) | ROC-AUC vs direct edges | AP vs direct edges | pairs with mean response > 0.01 |
|---:|---:|---:|---:|
| 1 | 1.000000 | 1.000000 | 8 |
| 2 | 0.996951 | 0.970486 | 11 |
| 4 | 0.963415 | 0.574932 | 12 |
| 8 | 0.954268 | 0.506728 | 3 |

**Result: PARTIAL / SCALE DEPENDENT.** Temporal coarse-graining introduces mediated responses into the observed relation. A direct one-step relation is therefore not guaranteed to remain a sparse direct relation at a longer temporal scale.

This is not a failure of intervention causality. It is evidence that **directness is defined relative to a temporal resolution**.

## 6. Intervention-amplitude robustness

At q=1, delta was varied while the same nonlinear system and intervention protocol were retained.

| delta | ROC-AUC | AP | mean direct response | mean null response |
|---:|---:|---:|---:|---:|
| 0.05 | 1.000000 | 1.000000 | 0.408494 | 0.000000 |
| 0.15 | 1.000000 | 1.000000 | 0.408089 | 0.000000 |
| 0.30 | 1.000000 | 1.000000 | 0.406506 | 0.000000 |
| 0.60 | 1.000000 | 1.000000 | 0.400000 | 0.000000 |
| 1.20 | 1.000000 | 1.000000 | 0.375986 | 0.000000 |

**Result: PASS for support, NOT invariant in magnitude.** The direct relation remains identifiable, while effective response per unit intervention decreases as nonlinear saturation grows.

## 7. Null / interpretation

The experiment does not establish that a universal physical relation exists independently of representation. It establishes a narrower operational fact:

> In the tested nonlinear dynamical system, a controlled source→target response is a more stable object than its numerical coefficient. Element-preserving coordinate changes preserve relation support; changing temporal resolution changes what counts as direct.

This strengthens the working representation of relation as a **response structure** rather than a universal scalar edge weight.

## 8. Current property table

| property | status | evidence |
|---|---|---|
| reproducible source→target response | SUPPORTED | intervention experiments |
| distinguishes direct from null pairs in controlled nonlinear model | SUPPORTED | AUC/AP = 1 at q=1 |
| invariant under element-wise invertible coordinate change | SUPPORTED IN MODEL | 3 representations, AUC/AP = 1 |
| invariant under element relabeling / permutation | SUPPORTED IN MODEL | AUC/AP = 1 |
| universal numerical relation strength | NOT SUPPORTED | response magnitude changes with representation and delta |
| directness independent of temporal scale | REFUTED IN MODEL | q>1 produces mediated responses |
| proof of ontological physical relation | NOT ESTABLISHED | simulations are models, not experiments on nature |

## 9. Next decisive direction

The next stronger test should remove the known-model advantage: use an unknown continuous medium, blind held-out interventions, unknown spatial relabeling, and compare whether the same response-structure equivalence can be recovered without access to the generating interaction matrix.
