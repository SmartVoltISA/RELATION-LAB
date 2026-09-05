# RELATION-FUNDAMENTAL-011 — Observational Equivalence of Different Internal Realizations

Date: 2026-09-05
Status: COMPLETE — NEGATIVE / LIMIT RESULT

## Question

Can two internally different systems have exactly the same observable dynamics, so that internal elements and internal relations cannot be uniquely inferred from observations?

## Locked construction

Model A is a 2-state linear dynamical system:

A = [[0.72, 0.18], [-0.11, 0.61]]
B = [[0.35], [0.12]]
C = [1, 0]

The observed signal is y = Cx.

Model B is a 3-state realization containing the same observable 2-state subsystem plus an unobserved hidden state z:

A_B = blockdiag(A, 0.43)
B_B = [0.35, 0.12, 0]^T
C_B = [1, 0, 0]

The hidden state has internal dynamics but is completely unobservable.

Model C is a 4-state realization containing the same observable subsystem plus two hidden states with a different internal relation:

A_hidden = [[0.43, 0.27], [0, 0.31]]

The hidden relation z2 -> z1 is therefore present in Model C but absent in Model A.

All models receive exactly the same input sequence.

T = 2000, seed = 20260905.

## Numerical comparison

| Test | A vs B | A vs C |
|---|---:|---:|
| Maximum absolute difference in observed y | 0.000000000000000 | 4.44e-16 |
| Observable trajectory equivalence | YES | YES |
| Impulse response first 5 values | identical | identical |
| Impulse-response energy | 0.276391002 | 0.276391002 |
| Observable input-output distinction | NONE | NONE |

Impulse response after a unit input at t=100:

| Lag | Model A | Model B | Model C |
|---:|---:|---:|---:|
| 1 | 0.350000 | 0.350000 | 0.350000 |
| 2 | 0.273600 | 0.273600 | 0.273600 |
| 3 | 0.203238 | 0.203238 | 0.203238 |
| 4 | 0.144724 | 0.144724 | 0.144724 |
| 5 | 0.099197 | 0.099197 | 0.099197 |

## Interpretation

The three models have different internal dimensionality and different internal relations, yet every accessible observable used in this experiment is identical to numerical precision.

Therefore an observer restricted to y and the applied input cannot uniquely recover:

- the number of hidden elements;
- the existence of hidden internal relations;
- the detailed internal relation matrix;
- the mechanism realizing the observable response.

This is a genuine identifiability limit, not an algorithm failure.

## Important distinction

This result does NOT say that relations are unreal.

It says that an internal relation is not automatically an observable invariant.

A hidden relation can be physically present in one realization and absent in another while the two realizations have exactly the same observable behavior.

Therefore the strongest experimentally defensible object is an observable response equivalence class.

## Consequence for the working definition

The previous definition must be split into two levels.

### Observable relation

A relation is experimentally established when its intervention-response signature is reproducible on accessible observables.

### Internal relation

An internal relation is a hypothesis about the mechanism producing that signature. It requires additional observables or interventions that break the equivalence class.

## Strong conclusion

For a given observation and intervention interface:

`same complete input-output behavior` implies `no experiment through that interface can distinguish the internal realizations`.

Therefore no algorithm can recover a unique hidden relation from data that are exactly observationally equivalent.

## What this changes

This gives us a hard boundary for the entire RELATION-LAB program.

We should no longer ask only:

"What is the true internal connection?"

We should ask:

"What relational structure is invariant across all realizations compatible with the observations?"

That invariant observable structure is a stronger candidate for a fundamental relation than any particular hidden edge.

## Next decisive experiment

Construct two observationally equivalent realizations and then enlarge the intervention/observation interface until the equivalence breaks. Measure exactly which new observable quantity is sufficient to distinguish them.

This will test whether relation is best defined relative to an experimental interface, or whether there is a deeper interface-independent invariant.
