# RELATION-FUNDAMENTAL-009 — Invariant Dynamics, Composition, and Quantum Control

Date: 2026-09-05
Status: COMPLETE CURRENT EXPERIMENT

## Purpose

Push the relation definition beyond pairwise graph language. Test whether the strongest candidate is a response operator with composition, coordinate covariance, finite-resolution behavior, and causal direction; then test the distinction between correlation and influence in a two-qubit quantum model.

## A. Classical operator covariance

A 12-state stable directed linear dynamical system was constructed with spectral radius 0.82. The physical impulse-response operator at delay tau is A^tau.

An invertible dense coordinate transformation y=Mx was applied. The transformed operator is A_y=M A M^-1.

| Test | Result |
|---|---:|
| Max covariance error, tau in {1,2,4,8} | 8.44e-15 |
| Eigenvalue/physical dynamics preservation | PASS |

Individual matrix entries changed under M, but the correctly transformed physical input-output predictions remained invariant to numerical precision.

## B. Composition of relation responses

For the same Markovian linear system, response operators were checked against the semigroup/composition law:

`R(t1+t2) = R(t2) R(t1)`.

| t1 | t2 | Maximum composition error |
|---:|---:|---:|
| 1 | 1 | 0.0 |
| 1 | 2 | 0.0 |
| 2 | 2 | 0.0 |
| 4 | 4 | 0.0 |

This is an exact property of the model. It means a response relation is not merely a static association; it can compose through time.

## C. Causal onset and path length

The same system was treated as an unknown directed network. For every reachable ordered pair, the earliest nonzero impulse-response time was compared with the directed shortest-path length in the generating graph.

| Quantity | Result |
|---|---:|
| Reachable ordered pairs tested | 58 |
| Exact onset/path-length agreement | 58/58 |
| Agreement fraction | 1.000 |

This shows that, in this model, temporal response contains structural distance information even when distance is not given as a geometric coordinate.

Important qualification: this is a property of the chosen causal dynamics, not proof that physical spatial distance is always emergent from temporal response.

## D. Coarse-grained observables

The fine system was observed through six block-averaged variables. The coarse response was computed as C A^tau B, where C averages target blocks and B applies equal source-block perturbations.

The fine and coarse descriptions produce different numerical coefficients, but the coarse prediction is exactly the projection of the same underlying operator. Thus loss of individual edges under coarse-graining is compatible with preservation of observable predictions.

## E. Quantum no-signalling control

A two-qubit Bell state |Phi+> was used as a deliberately correlated state. A local unitary intervention was applied only to subsystem A.

First, there was no interaction Hamiltonian between A and B. Then an interaction Hamiltonian was introduced:

`H = 0.7 Z⊗Z + 0.2 X⊗I`.

The reduced state of B was compared before and after the local intervention.

| Condition | Norm of change in B marginal |
|---|---:|
| Entangled state, no interaction | 1.96e-17 |
| Entangled state, with interaction | 0.234323 |

The first value is numerical zero. The Bell-state correlation alone does not allow a local operation on A to change B's reduced state. With dynamical interaction, the same intervention produces a finite B response.

Conclusion: correlation, even strong quantum correlation, is not by itself operational influence. The response criterion survives this conceptual extension.

## F. What the combined tests establish within the tested models

| Property | Status |
|---|---|
| Relation represented by response rather than scalar coefficient | supported |
| Coordinate covariance of physical response | supported |
| Static matrix-edge invariance under arbitrary mixing | not supported |
| Temporal composition of response | supported in Markovian model |
| Directionality | supported |
| Structural delay/distance encoded in response onset | supported in tested network |
| Coarse-graining changes numerical strength | supported |
| Observable predictions can survive coarse-graining | supported |
| Correlation implies influence | refuted |
| Quantum entanglement alone implies signalling/influence | refuted in control |
| Interaction produces intervention response | supported |

## G. Updated conceptual result

The strongest candidate is not a pairwise number and not a graph edge. It is a transformation of conditional future behavior under a change of state.

A compact form is:

`R(delta | S, tau, O)`

where S is the state, delta is the intervention or exogenous perturbation, tau is the delay, and O is the chosen observation map.

A directed pairwise relation is a special case obtained when the intervention and observation maps isolate two distinguishable degrees of freedom.

The physically meaningful object is therefore closer to an operator between possible responses than to a scalar connection strength.

## H. Remaining unresolved questions

The following are still not established:

1. Whether an invariant response object exists for arbitrary nonlinear and stochastic systems, not merely the tested classes.
2. Whether the notion can be formulated without selecting any privileged state variables.
3. Whether a fully continuous relativistic field admits an operational relation object with the same invariance properties.
4. How the definition changes in quantum field theory, where subsystem boundaries and observables are constrained by the theory.
5. Whether causal influence is fundamental, or whether it is itself a derived property of a deeper dynamical structure.
6. Whether physical space can be reconstructed uniquely from relation-response data rather than merely in selected models.

## Final status

PASS for the tested mathematical and quantum-control models.

The evidence increasingly favors this working statement:

**A relation is not the number connecting two elements. It is the reproducible transformation of the system's conditional future response produced by a distinguishable change in state.**

The scalar coefficient, graph edge, spatial distance, or correlation value is a representation or projection of that deeper response structure.

This remains an operational research result, not an ontological proof about the universe.
