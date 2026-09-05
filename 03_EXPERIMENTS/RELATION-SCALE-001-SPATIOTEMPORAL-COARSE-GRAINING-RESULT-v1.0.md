# RELATION-SCALE-001 — Spatiotemporal Coarse-Graining Result v1.0

## Status
**EXECUTED / CONTROLLED SYNTHETIC RESULT**

## Question
Does a relation retain an identifiable structure when both spatial and temporal resolution are changed?

## Design
A known directed dynamical process was observed at multiple spatial resolutions and multiple temporal sampling intervals. The relation was evaluated from controlled intervention response rather than from raw correlation.

Spatial resolutions: 40, 20, 10, 8, 5, 4 effective elements.
Temporal resolutions: 1, 2, 4, 8 simulation steps.

The source and target were distinct at fine resolution and were progressively merged by spatial coarse-graining.

## Result
The directed relation remained identifiable while source and target occupied distinct coarse cells and the temporal sampling remained below the response-memory scale. Once the coarse cells merged, directed source-to-target identity became non-identifiable.

| Spatial resolution | Temporal step | Direction identifiable | Sign retained | Relative response magnitude |
|---:|---:|:---:|:---:|---:|
| 40 | 1 | YES | YES | 1.000 |
| 20 | 1 | YES | YES | 0.500 |
| 10 | 1 | YES | YES | 0.250 |
| 8 | 1 | PARTIAL | YES | 0.200 |
| 5 | 1 | NO | NO | merged |
| 4 | 1 | NO | NO | merged |
| 20 | 2 | YES | YES | 0.500 |
| 20 | 4 | YES | YES | 0.500 |
| 20 | 8 | PARTIAL | YES | 0.500 |

The response amplitude decreases approximately with the spatial averaging factor while the source-target direction survives until the two elements are represented by the same coarse cell.

## Interpretation
The experiment separates two concepts:

1. **Existence of a dynamical influence in the generating system.**
2. **Identifiability of that influence from a chosen observation scale.**

Coarse-graining can destroy identifiability without demonstrating that the underlying interaction disappeared.

Temporal coarse-graining produces a second boundary: when sampling becomes comparable to or longer than the response-memory timescale, the direction can become ambiguous even when spatial separation remains available.

## Important conclusion
The numerical value of a local coupling coefficient is not invariant under coarse-graining. A more robust candidate is the **response structure**: source, target, sign, lag ordering, and reproducibility under intervention.

## What is supported
- Relation is operationally observable as a controlled response pattern.
- Relation has a scale of observability.
- Spatial and temporal resolution affect identifiability.
- Loss of identifiability is not equivalent to loss of the underlying dynamical influence.
- A universal scalar relation strength is not supported by this experiment.

## What is not supported
- No claim that the result applies to all physical systems.
- No claim that relation is ontologically fundamental.
- No claim that particles are emergent from relation.
- No claim that a continuum has a unique observer-independent relation field.

## Next test
Test **representation invariance of the response structure itself** under independent nonlinear coordinate transforms, spatial remapping, and time reparameterization, using held-out interventions and explicit null models. The target is an invariant object weaker than a scalar K but stronger than raw correlation.
