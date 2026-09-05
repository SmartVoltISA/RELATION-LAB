# RELATION-CONTINUUM-001 — Decomposition and Continuum Sweep

Date: 2026-09-05
Status: COMPLETE CURRENT TEST

## Question

If one continuous dynamical field is divided into different sets of elements, what belongs to the relation itself and what belongs only to the chosen decomposition?

## Model

A 120-element periodic discretization represents a continuous-like scalar field.

Dynamics:

`x[t+1] = A x[t] + noise`

with spectral radius 0.8856123. The background contains the same local couplings for every location, while one weak directed contribution is added from source 17 to target 83 with K = 0.025.

The experiment is not intended to claim that the 120-point discretization is a physical continuum. It tests whether the inferred relation changes under observation/decomposition while the underlying dynamical operator remains the same.

## Test A — Spatial/coarse partitions

The same field was represented by contiguous blocks of different sizes. A block intervention perturbs all fine elements in the source block and the target response is averaged over the target block.

| Block size | Number of elements | Source block | Target block | Source/target distinct | Hidden response score |
|---:|---:|---:|---:|---|---:|
| 1 | 120 | 17 | 83 | yes | 2.000000e-03 |
| 2 | 60 | 8 | 41 | yes | 5.000000e-04 |
| 3 | 40 | 5 | 27 | yes | 2.222222e-04 |
| 4 | 30 | 4 | 20 | yes | 1.250000e-04 |
| 5 | 24 | 3 | 16 | yes | 8.000000e-05 |
| 6 | 20 | 2 | 13 | yes | 5.555556e-05 |
| 10 | 12 | 1 | 8 | yes | 2.000000e-05 |
| 12 | 10 | 1 | 6 | yes | 1.388889e-05 |
| 15 | 8 | 1 | 5 | yes | 8.888889e-06 |
| 20 | 6 | 0 | 4 | yes | 5.000000e-06 |
| 30 | 4 | 0 | 2 | yes | 2.222222e-06 |
| 40 | 3 | 0 | 2 | yes | 1.250000e-06 |
| 60 | 2 | 0 | 1 | yes | 5.555556e-07 |
| 120 | 1 | 0 | 0 | no | 1.388889e-07 |

The hidden contribution remains present under every partition in which source and target remain distinguishable, but its measured magnitude decreases approximately with target-region averaging. When source and target are merged into the same element, directed source-target identification is lost.

## Test B — Random decompositions

The same 120 fine elements were randomly partitioned into k groups, with no spatial information supplied to the partition.

Across 200 random partitions per k, the probability that the source and target landed in the same coarse element was approximately 1/k, as expected for random grouping.

| Number of groups | Same-element fraction | Mean target response score |
|---:|---:|---:|
| 2 | 0.470 | 5.555556e-07 |
| 3 | 0.295 | 1.250000e-06 |
| 4 | 0.205 | 2.222222e-06 |
| 5 | 0.185 | 3.472222e-06 |
| 6 | 0.140 | 5.000000e-06 |
| 8 | 0.085 | 8.888889e-06 |
| 10 | 0.085 | 1.388889e-05 |
| 12 | 0.055 | 2.000000e-05 |
| 15 | 0.050 | 3.125000e-05 |
| 20 | 0.040 | 5.555556e-05 |
| 30 | 0.020 | 1.250000e-04 |
| 40 | 0.010 | 2.222222e-04 |
| 60 | 0.010 | 5.000000e-04 |

Interpretation: arbitrary grouping can destroy identifiability by merging source and target. This is not disappearance of the underlying dynamical effect; it is loss of resolution in the chosen observable decomposition.

## Test C — Operator representation invariance

A random invertible linear transformation `y = Mx` was applied to the same dynamical system. The transformed operator was `A_y = M A M^-1`.

The following were checked:

| Quantity | Result |
|---|---:|
| Maximum eigenvalue-set discrepancy | 1.19e-09 |
| Physical response tau=1 discrepancy | 1.82e-14 |
| Physical response tau=2 discrepancy | 3.59e-14 |
| Physical response tau=4 discrepancy | 5.56e-14 |
| Physical response tau=8 discrepancy | 5.90e-14 |

The sparse matrix representation is not invariant under arbitrary coordinate mixing, but the underlying linear operator and correctly transformed physical input/output experiment are invariant to numerical precision.

## Test D — What survives decomposition?

Three levels must be distinguished.

1. **Pairwise matrix entry:** depends strongly on the selected element decomposition.
2. **Response between chosen regions/elements:** survives as long as the relevant source and target remain distinguishable and the measurement resolution is sufficient.
3. **Full dynamical response operator:** is the strongest candidate for decomposition-independent content. Different coordinate representations describe the same operator through a change of basis.

## Main finding

The experiment does not support the idea that a particular graph edge or matrix coefficient is the most fundamental object.

It supports a more precise statement:

**The experimentally stable object is the transformation of possible responses under a perturbation; its numerical matrix representation depends on how the system is decomposed and measured.**

Coarse-graining does not necessarily destroy the underlying relation, but it can make a particular source-target relation unidentifiable because source and target become merged or the response is averaged below detection resolution.

## Important limitation

This test still starts with a scalar field and a chosen discretization. It therefore does not prove that physical space is emergent from relations, nor that the decomposition into electrons, fields, regions, or particles is arbitrary in nature.

It does establish a falsifiable methodological distinction:

`representation-dependent relation coefficient`

versus

`representation-covariant response operator`.

The second survives coordinate changes when interventions and observations are transformed consistently.

## Consequence for the working definition

The current definition should be upgraded from a pairwise scalar to a response object:

`R(i -> j | state, intervention, time, resolution)`

and, for a continuous field,

`R(r -> r', tau | state, intervention, resolution)`.

A scalar K is a local projection of this object, not the relation itself.

## Remaining decisive test

The next unresolved issue is not another graph detector. It is whether a relation can be defined and recovered when the underlying continuous field has no privileged decomposition at all, and only invariant observables are available. That requires testing field-level perturbation/response operators under multiple incompatible discretizations and checking whether the same physical predictions are recovered without identifying individual matrix edges.
