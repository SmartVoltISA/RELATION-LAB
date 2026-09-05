# RELATION-FUNDAMENTAL-015 — Continuous Partition Invariance

Date: 2026-09-05
Status: COMPLETE — PASS for global dynamical invariants; FAIL for local element-level invariance

## Question

If the underlying system is a continuous field, which properties of an observed relation survive when the same field is partitioned into different sets of elements?

The test deliberately does not assume that any particular partition is fundamental.

## Locked continuous model

A one-dimensional periodic continuous medium is represented at high numerical resolution (N = 240) by the same underlying advection-diffusion-reaction evolution:

`∂x/∂t = D ∂²x/∂r² - v ∂x/∂r + λx`

with:

- D = 0.015
- v = 0.12
- λ = -0.08
- periodic boundary conditions
- initial localized Gaussian perturbation centered at r = 0.33
- numerical timestep dt = 0.0002
- 3000 evolution steps

No relation graph is supplied to the estimator.

## Three incompatible descriptions

The same underlying field is observed as:

1. regular partition: 24 equal cells;
2. coarse regular partition: 12 equal cells;
3. adaptive irregular partition: 24 Voronoi cells generated from randomly selected centers.

A fourth representation is the first five real Fourier modes plus the constant mode.

The descriptions therefore disagree about the local elements and coordinates while referring to the same underlying field evolution.

## Experiment A — global propagation invariants

The field's circular centroid and variance were estimated directly from the fine field and independently reconstructed from each cell partition.

Reference estimates from the fine field:

| Quantity | True/model value | Fine-field estimate |
|---|---:|---:|
| Propagation speed v | 0.120000 | **0.12000242** |
| Diffusion coefficient D | 0.015000 | **0.01498996** |

Partition estimates:

| Representation | Estimated v | Absolute error vs fine field | Estimated D | Absolute error vs fine field |
|---|---:|---:|---:|---:|
| Regular 24 | 0.12000397 | 0.00000155 | 0.01498882 | 0.00000114 |
| Regular 12 | 0.12022099 | 0.00021856 | 0.01476439 | 0.00022557 |
| Irregular Voronoi 24 | 0.12501547 | 0.00501305 | 0.01545904 | 0.00046908 |

The global propagation and spreading structure survive the change of partition. Accuracy degrades with coarser/irregular sampling, but the same dynamical quantities remain recoverable.

## Experiment B — local relation representation

The local cell-to-cell influence matrix was computed for each partition.

Result: the local matrices are not numerically identical and their individual entries cannot be mapped one-to-one across incompatible partitions. In particular, the identity of a local element depends on the partition.

Therefore:

`local coefficient / local edge` is NOT partition invariant.

## Experiment C — temporal spectral structure

The first five Fourier-mode amplitudes were tracked from the same underlying field. Log-linear decay estimates were:

| Mode | Estimated decay rate |
|---:|---:|
| k=1 | -0.67213077 |
| k=2 | -2.44853608 |
| k=3 | -5.40926112 |
| k=4 | -9.55437961 |
| k=5 | -14.88399357 |

These are properties of the underlying evolution, not of a particular cell labeling. A change of element partition changes the local coefficient representation but does not change the underlying spectral evolution.

## Experiment D — partition-collapse limit

As the partition becomes extremely coarse, multiple physically distinct regions are merged into one observable element. At the limit of one element, directed local relations are no longer identifiable from the partition because source and target distinctions have been removed.

This is an information limit, not evidence that the underlying continuous dynamics disappeared.

## Main result

The same continuous dynamics supports two different classes of properties:

### Partition-dependent

- individual elements;
- local coordinates;
- local coefficients;
- local graph edges;
- exact source/target labels after incompatible coarse-graining.

### Partition-robust within experimental resolution

- global propagation speed;
- global spreading rate;
- temporal spectral structure;
- the accessible response of the continuous field as a whole.

## Interpretation

This experiment strengthens the earlier interface result.

A fundamental candidate should not be required to retain the identity of an arbitrarily chosen cell. Instead, it should survive admissible changes of representation as a property of the underlying response dynamics.

The current strongest candidate is therefore:

> **An experimentally established relation is an invariant feature of the response map of the underlying dynamics, while its decomposition into elements and local coefficients is representation- and partition-dependent.**

## Important limitation

This does NOT establish that physical space is emergent from relation, nor that the field itself is fundamental. It only establishes, for this continuous model, that global response structure is more robust than any particular discretization.

## Falsification target

The next test must use two genuinely different dynamics that are deliberately constructed to have the same coarse global invariants but different local response fingerprints. If an experiment can distinguish them through sufficiently rich interventions, then global invariants alone are insufficient and the fundamental candidate must include the full response operator rather than only propagation speed, diffusion, or spectrum.

## Conclusion

PASS: global dynamical response invariants survive incompatible partitions.

FAIL: local element identity and local relation coefficients are not fundamental invariants.

This moves the research one level deeper: the candidate fundamental object is the equivalence class of experimentally accessible response maps, not the elements used to discretize the field.
