# RELATION-FUNDAMENTAL-014 — Interface Invariant of an Observable Relation

Date: 2026-09-05
Status: COMPLETE — PASS for representation invariance; FAIL for hidden internal uniqueness

## Question

What survives when the same dynamical system is described in different coordinates and observed through different interfaces?

The test separates three claims:

1. a relation signature can be invariant under a reversible change of representation;
2. the same internal relation can become unidentifiable after information is removed;
3. therefore the strongest invariant is the accessible response map, not a particular internal coefficient or edge.

## Locked system

Four internal states are used.

A = [[0.72, 0.18, 0, 0],
     [-0.11, 0.61, 0, 0],
     [0, 0, 0.43, 0.27],
     [0, 0, 0, 0.31]]

External input enters the first two states:

B = [[0.35], [0.12], [0], [0]]

Observable output in the original representation:

y = x1

The internal directed relation is z2 -> z1 with coefficient +0.27.

## Representation test

A random invertible matrix M defines a second representation:

y_state = M x

The transformed dynamics are:

A' = M A M^-1
B' = M B
C' = C M^-1

The intervention source direction and target readout are transformed consistently. No information is discarded.

## Result: reversible representation

| Test | Result |
|---|---:|
| Max difference in external impulse response | **1.11e-16** |
| Max difference in internal relation response after consistent transformation | **1.67e-16** |
| Original relation response, lag 1 | **0.270000** |
| Transformed relation response, lag 1 | **0.270000** |
| Representation invariance | **PASS** |

Impulse response of the external observable:

| Lag | Original | Transformed |
|---:|---:|---:|
| 1 | 0.350000 | 0.350000 |
| 2 | 0.273600 | 0.273600 |
| 3 | 0.203238 | 0.203238 |
| 4 | 0.144724 | 0.144724 |
| 5 | 0.099197 | 0.099197 |
| 6 | 0.065503 | 0.065503 |
| 7 | 0.041588 | 0.041588 |
| 8 | 0.025246 | 0.025246 |

The coordinate entries of A and A' are different, but the accessible physical response is identical.

## Hidden-realization control

A second internal realization changes only the hidden 2x2 block:

A_hidden_alt = [[0.51, -0.22],
                [0.14, 0.28]]

The external input-output behavior remains exactly identical because the hidden subsystem is not coupled to the observable subsystem.

| Test | Result |
|---|---:|
| Max difference in external trajectory | **0** |
| Max difference in external impulse response | **0** |
| External interface distinguishes realizations | **NO** |
| Hidden z2 -> z1 response: original | **+0.270000** |
| Hidden z2 -> z1 response: alternative | **-0.220000** |
| Difference under expanded hidden interface | **0.490000** |

## Interface ladder

| Interface | Accessible observation | Accessible intervention | Result |
|---|---|---|---|
| I0 | external y | external u | internal realizations equivalent |
| I1 | z1 | external u | still equivalent |
| I2 | z1 | z2 | realizations distinguishable |
| I3 | z1,z2 | z1,z2 | direction distinguishable |

## Interpretation

Three different mathematical objects must be separated.

### Internal coefficient

A number such as +0.27 in one representation. It changes under coordinate transformation and is therefore not itself the invariant relation.

### Internal relation

A directed dependency inside one realization. It may be real within that realization while remaining inaccessible from a restricted interface.

### Observable relation signature

The complete accessible response of the system to an allowed intervention. Under a reversible change of coordinates with the intervention and observation maps transformed consistently, this signature is unchanged.

## Main result

For the locked model, the following statement survives all tests:

> The invariant object is the accessible intervention-to-observation response map, not the coordinate coefficient used to represent it.

At the same time, this map is relative to the experimental interface. If the interface discards the variables carrying the relation, the relation becomes non-identifiable even though it remains present in one internal realization.

## Mathematical form

For an interface I, define:

F_I : (intervention, initial accessible state) -> distribution of accessible observations over time.

Two realizations are observationally equivalent under I when their F_I maps are identical for every intervention permitted by I.

An experimentally established relation is therefore an invariant feature of F_I under admissible reparameterizations of the same interface.

## Consequence

The strongest candidate for a fundamental relation is not a universal edge or scalar coefficient. It is an equivalence-invariant feature of the system's intervention-response map.

This is stronger than the earlier definition because it explicitly handles representation changes and hidden internal realizations.

## Remaining unresolved issue

We have not shown that there exists an interface-independent relation. The present result instead establishes a hard methodological boundary:

- representation changes can preserve the response structure;
- information loss can destroy identifiability;
- hidden internal mechanisms are not uniquely recoverable from equivalent observables.

Therefore any claim of an interface-independent ontological relation requires an additional physical principle or a family of interfaces whose union is demonstrably complete for the phenomenon under study.

## Next test

Use a genuinely continuous field and compare multiple incompatible partitions, observation functions, and intervention bases while preserving the same underlying physical evolution. Search for response features that survive every admissible partition rather than tracking any predefined element.
