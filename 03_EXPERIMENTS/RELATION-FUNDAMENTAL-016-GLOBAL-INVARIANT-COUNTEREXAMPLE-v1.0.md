# RELATION-FUNDAMENTAL-016 — Global-Invariant Counterexample

Date: 2026-09-05
Status: COMPLETE — PASS for the counterexample; global invariants are insufficient to identify local relations

## Question

Can two systems have the same global dynamical invariants while possessing different local response structures?

If yes, global propagation speed, spectrum, trace, norm and aggregate response cannot by themselves be the definition of relation.

## Construction

N = 40.

System A is a symmetric nearest-neighbour ring operator A:

- diagonal = -0.4
- nearest neighbours = +0.2
- periodic boundary conditions

System B is constructed by an orthogonal similarity transform:

`B = Q A Q^T`

where Q is a fixed random orthogonal matrix generated with seed 20260905.

The two systems therefore have exactly the same eigenvalues and all similarity invariants, while their local matrix representations differ strongly.

The discrete response operator is `M = exp(dt A)` with dt = 0.5; for B, `M_B = exp(dt B)`.

No relation graph is supplied to an observer.

## Global invariants

| Quantity | System A | System B | Difference |
|---|---:|---:|---:|
| N | 40 | 40 | 0 |
| trace(A) | -16.000000000000 | -16.000000000000 | 3.55e-15 |
| Frobenius norm | 3.098386676966 | 3.098386676966 | 0 |
| max eigenvalue mismatch | | | 7.77e-16 |
| min eigenvalue mismatch | | | 7.77e-16 |
| eigenvalue set | identical | identical | numerical zero |

For 1000 isotropic random initial states, the mean one-step response norm was:

| Statistic | A | B |
|---|---:|---:|
| Mean ||Mx|| | 5.23750899 | 5.23670814 |
| Standard deviation | 0.61452992 | 0.62896614 |

These aggregate statistics are close, while the exact similarity invariants are identical.

## Local response test

A unit perturbation was applied to each source separately and the complete target response vector was recorded.

For System A, 99.751% of off-source response energy is concentrated in the two nearest neighbours for every source.

For System B, the corresponding mean fraction is only 3.319% and varies across sources.

| Local metric | System A | System B |
|---|---:|---:|
| Mean off-source response energy | 0.01357480 | 0.01282217 |
| Mean fraction in nearest neighbours | **0.99751175** | **0.03319332** |
| Mean number of targets with |response| > 0.001 | **4.0** | **37.1** |
| Mean off-source L1 response | 0.17306145 | 0.56435963 |

For source 0, the one-step response was:

System A:

- source 0: +0.82693855
- target 1: +0.08228312
- target 39: +0.08228312
- target 2: +0.00410732
- target 38: +0.00410732

System B:

- source 0: +0.82562331
- target 33: -0.02967343
- target 30: -0.02966813
- target 18: +0.02939324
- target 8: +0.02630735

The response-vector correlation for this particular source was 0.981605 because the large self-response dominates the vector. This does not erase the strong difference in off-source spatial distribution.

## Interpretation

This is a deliberate counterexample to the hypothesis that global dynamical invariants are sufficient to define relation.

The systems have the same spectrum and similarity invariants, but their local response structures differ.

Therefore:

`global invariant` != `local relation`

A global quantity can characterize the dynamical class without specifying the internal relation structure.

## Relation to wave / field intuition

System B can visually resemble a distributed or wave-like response because a local perturbation is represented across many coordinates rather than being confined to nearest neighbours.

However, this experiment does NOT establish an electromagnetic field or a physical wave. System B is an abstract dynamical system related to A by a change of basis. The visual spread is evidence about representation and response structure, not about physical ontology.

The correct statement is:

> A distributed response pattern can arise without a local graph edge structure being fundamental.

## Main conclusion

PASS for the counterexample.

Two systems can share global dynamical invariants while differing substantially in local relation structure. Therefore the fundamental candidate cannot be only propagation speed, diffusion coefficient, spectrum, trace, energy, autocorrelation, or another small set of global scalars.

The candidate must retain richer information about the experimentally accessible response map.

## Consequence for the research program

The next target is no longer to find a smaller global scalar.

The next target is to determine the minimal equivalence object containing enough response information to preserve experimentally distinguishable relations.

Candidate:

`full response operator modulo experimentally invisible transformations`

This is stronger than a graph, a matrix entry, or a global invariant.

## Important limitation

Because B was constructed by a similarity transformation, the experiment does not show that two physically distinct universes can have identical global invariants. It shows the mathematical insufficiency of global invariants for reconstructing local relation structure.

The next stronger test should use genuinely different dynamical generators, not merely a basis-related pair, while matching a chosen set of global observables.
