# RELATION-INVAR-001 — Representation Invariance of Relation v1.0

## Status
**EXECUTED / NUMERICAL RESULT / MIXED**

## Question
Does the operational relation survive a change of representation? We distinguish element-preserving transformations from transformations that mix the elements.

## Model
N=8 nonlinear variables, T=4000–5000.
Hidden directed edges:
`0→1 (+0.7), 1→2 (-0.5), 2→3 (+0.4), 4→3 (+0.6), 3→5 (-0.55), 5→6 (+0.45), 4→7 (-0.35)`.

Dynamics:
`x[t+1] = tanh(A x[t] + 0.35 x[t] + 0.18 noise)`.

Representations:
1. X — original variables.
2. Y — invertible component-wise transform `Y_i=sinh(X_i)`.
3. Z — mixed coordinates `Z=M X`, random invertible linear mixing.

A lag-1 estimator was fit in each representation and evaluated against the known generating support.

## Five-seed component-wise test

| Seed | X AUC | Y AUC | X AP | Y AP |
|---:|---:|---:|---:|---:|
| 100 | 0.99749 | 0.99749 | 0.98214 | 0.98214 |
| 101 | 0.98246 | 0.98747 | 0.92857 | 0.94048 |
| 102 | 0.98747 | 0.98997 | 0.94048 | 0.94805 |
| 103 | 0.98747 | 0.98997 | 0.94048 | 0.94805 |
| 104 | 0.98496 | 0.98747 | 0.93407 | 0.94048 |

Mean X AUC = 0.98797; mean Y AUC = 0.99048; mean difference = +0.00251.

## Mixed-coordinate control

Seed 42:

| Representation | AUC vs original edge labels |
|---|---:|
| X | 0.98246 |
| Y=sinh(X) | 0.97995 |
| Z=M X | 0.54887 |

Coefficient count above `|coef|>0.05`:
- Y: 15/64
- mixed Z: 58/64

## Intervention support

For seed 42, local one-step interventions on every source gave the same nonzero-support count in X and Y (15/64). Magnitudes changed under the nonlinear observation transform.

## Interpretation

An invertible component-wise change of variables preserves element identity and empirically preserves causal support. Numerical relation strength is not unchanged, but direct source→target structure remains recoverable.

A transformation that mixes elements destroys the original sparse pairwise decomposition: the same underlying dynamics become distributed across many transformed coordinates. Therefore a pairwise scalar relation is not representation-free.

## Conclusions

**PASS:** robustness under element-preserving invertible reparameterization.

**FAIL:** universal coordinate-independence of a pairwise scalar relation.

The strongest current formulation is therefore a **relational response structure relative to an identified decomposition into elements/observables**, with transformation rules under reparameterization.

This does not establish that particles are fundamental elements, that relation is ontologically fundamental, or that a unique decomposition of a continuous physical field exists.

## Next decisive experiment

Test resolution/coarse-graining invariance: generate the same medium at fine resolution, aggregate neighboring elements, and measure which relational properties survive: direction, sign, causal reach, response ordering, and conservation-like quantities.
