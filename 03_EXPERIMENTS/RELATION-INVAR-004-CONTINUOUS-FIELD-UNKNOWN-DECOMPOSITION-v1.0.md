# RELATION-INVAR-004 — Continuous Field / Unknown Decomposition

**Status:** EXECUTED / VERIFIED
**Date:** 2026-09-05

## Question
Can a hidden nonlocal relation be detected in a continuous spatial field without supplying a graph, interaction matrix, or element decomposition to the estimator?

## Locked model
A 1D periodic continuous field was discretized only for numerical integration (N=80 grid samples). The estimator was not given the interaction matrix or hidden relation list.

Dynamics:

x[t+1] = x[t] + dt[-0.25x + 0.18 Laplacian(x) + noise]

plus one hidden nonlocal directed coupling:

source r=12 -> target r=57, coefficient K=+0.25.

dt=0.1, intervention delta=0.3.

The hidden coupling contributes only at the target location and is therefore not a predeclared graph edge from the estimator's perspective.

## Blind intervention procedure

For each source location, held-out times were perturbed locally. The one-step response field was measured. No interaction matrix or edge list was used to calculate the score. The score was the absolute normalized target response.

The spatial field was treated as a field of locations rather than a set of named nodes.

## Result

| quantity | result |
|---|---:|
| grid locations | 80 |
| ordered source-target pairs scored | 6320 (off-diagonal) |
| hidden relation | 12 -> 57 |
| hidden coefficient | +0.25 |
| intervention delta | 0.30 |
| ROC-AUC | 1.000000 |
| AP | 1.000000 |
| response at hidden target (normalized) | +0.025000 |
| largest other off-diagonal response from source 12 | +0.018000 |
| shuffled-label AUC | approximately 0.50 (null) |

The hidden target response is larger than every other off-diagonal response from the same source in the immediate one-step probe. The local Laplacian produces neighboring responses (+0.018), while the nonlocal target gives +0.025.

## Interpretation

**PASS, with a strict scope.** A localized nonlocal relation can be recovered from intervention response in a continuous spatial field without supplying a graph or interaction matrix. The detected object is a spatial response pattern, not a graph edge.

This result supports the transition:

node/edge representation -> field response operator.

It does not prove that physical reality is fundamentally a continuous field, nor that every physical relation is nonlocal or localized in this way.

## Important limitation

The numerical grid is still a discretization used by the simulator. Therefore "unknown decomposition" means the estimator was not told a semantic element decomposition; it does not mean the numerical integration had no coordinates.

Also, the hidden coupling was deliberately strong enough (+0.25) to exceed the nearest-neighbor one-step response. A harder test must vary K and distance and determine the detection threshold against local propagation.

## Next decisive experiment

Sweep hidden coupling strength K and source-target distance, with randomized hidden targets and blind held-out interventions. Determine the detection boundary where nonlocal relation becomes indistinguishable from ordinary local propagation.

This is the next falsification-oriented test.
