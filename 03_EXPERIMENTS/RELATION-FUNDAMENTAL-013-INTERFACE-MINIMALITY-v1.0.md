# RELATION-FUNDAMENTAL-013 — Interface Minimality of Relation

Date: 2026-09-05
Status: COMPLETE — PASS for the locked model; establishes an interface-dependent identifiability boundary

## Question

What is the minimum experimental access required to establish an internal directed relation when two internal realizations are exactly equivalent on the originally available observables?

## Locked construction

Two 4-state linear systems share exactly the same observable subsystem.

Observable subsystem:

A_obs = [[0.72, 0.18], [-0.11, 0.61]]
B_obs = [[0.35], [0.12]]

The measured observable is y = x1.

Both systems also contain hidden states z1, z2 with diagonal dynamics 0.43 and 0.31.

System N (null): no internal relation z2 -> z1.

System R (relation): an additional coefficient +0.27 from z2 to z1.

Both systems receive the same external input u through the observable subsystem only. Hidden states start at zero.

## Interface I0: original observation and input only

Accessible:

- observe y
- control u
- no observation of z1 or z2
- no intervention on z1 or z2

T = 200, seed = 20260905, identical input sequence.

Result:

| Test | Result |
|---|---:|
| Maximum |y_N - y_R| | **0.000000000000000** |
| Observable trajectories distinguishable | **NO** |
| Observable input-output behavior | **identical** |

Therefore the internal relation is not identifiable through I0.

## Interface ladder

We then enlarge the interface one capability at a time.

| Interface | Observe | Intervene | Distinguishes N/R? |
|---|---|---|---|
| I0 | y | u | NO |
| I1 | z1 | u | NO |
| I2 | z1 | z2 | YES |
| I3 | z1,z2 | z2 and z1 | YES, direction test |

Observation of z1 alone is insufficient because hidden states start at zero and are not externally driven.

The first sufficient interface is therefore: **observe target z1 + intervene on source z2**.

## I2: source-to-target intervention

A unit intervention z2 <- z2 + 1 was applied at the start of the measurement window.

### Target response

| Lag | Null N | Relation R | Difference R-N |
|---:|---:|---:|---:|
| 0 | 0.000000 | 0.000000 | 0.000000 |
| 1 | 0.000000 | 0.270000 | 0.270000 |
| 2 | 0.000000 | 0.199800 | 0.199800 |
| 3 | 0.000000 | 0.111861 | 0.111861 |
| 4 | 0.000000 | 0.056144 | 0.056144 |
| 5 | 0.000000 | 0.026635 | 0.026635 |
| 6 | 0.000000 | 0.012226 | 0.012226 |
| 7 | 0.000000 | 0.005497 | 0.005497 |
| 8 | 0.000000 | 0.002438 | 0.002438 |

The first-step response is exactly the generating coefficient +0.27.

## Intervention amplitude control

The same source intervention was repeated at four amplitudes.

| Delta | Response at lag 1 | Response / Delta |
|---:|---:|---:|
| 0.25 | 0.067500 | 0.270000 |
| 0.50 | 0.135000 | 0.270000 |
| 1.00 | 0.270000 | 0.270000 |
| 2.00 | 0.540000 | 0.270000 |

The response scales linearly with intervention amplitude in this locked linear model.

## I3: direction control

Reverse intervention z1 <- z1 + 1 was applied while observing z2.

| Lag | Response z2 after intervention on z1 |
|---:|---:|
| 0 | 0.000000 |
| 1 | 0.000000 |
| 2 | 0.000000 |
| 3 | 0.000000 |
| 4 | 0.000000 |
| 5 | 0.000000 |
| 6 | 0.000000 |
| 7 | 0.000000 |
| 8 | 0.000000 |

Thus the accessible relation is specifically z2 -> z1, not z1 -> z2.

## Main result

The internal relation cannot be uniquely inferred from the original observable interface, even though it is physically present in one realization. The relation becomes identifiable exactly when the interface gains the ability to intervene on its source and observe its target.

This gives a concrete minimality result for the locked model:

**source intervention + target observation is sufficient; target observation without source intervention is insufficient.**

## Interpretation

This experiment sharpens the operational definition of relation.

A relation is not only a property of an internal model. Its experimental status depends on the interface through which the system can be distinguished and perturbed.

For an interface I, define an observable relation signature as the equivalence class of accessible response distributions under allowed interventions.

Two internal realizations are equivalent under I if every accessible intervention produces the same accessible observations.

An internal relation is identifiable under I only if introducing/removing that relation changes at least one accessible response.

## Strong conclusion

The phrase "the relation exists" is incomplete unless the level of description is specified.

The precise experimental statement is:

> A relation is established relative to an observation/intervention interface when changing the source produces a reproducible change in an accessible target response that cannot be reproduced by the matched null.

This does not imply that inaccessible internal relations are unreal. It establishes a strict distinction between **internal existence** and **experimental identifiability**.

## Relation to the broader program

This result supports the current hierarchy:

1. Internal realization: one possible mechanism.
2. Observable response structure: what the interface can establish.
3. Equivalence class: all internal realizations indistinguishable through that interface.
4. Invariant relation: structure preserved across admissible changes of representation and interface.

The next question is therefore not simply "can we detect a relation?" but:

**what response structure remains invariant when the observation and intervention interface itself is changed?**

That is the next falsification target for a genuinely fundamental definition of relation.
