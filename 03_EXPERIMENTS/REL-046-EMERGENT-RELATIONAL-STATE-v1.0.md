# REL-046: Emergent relational state

Date: 2026-09-07
Status: DEFINED

## Question

Can a state variable that changes future relational behavior be recovered as a derived quantity from relation history, without inserting an explicit memory/object/agent node?

## Constraint

Fundamental alphabet remains relation acts r in {-1,+1}. No memory bit, object identity, node state, or E_comp is supplied as a primitive.

## Operational construction

For a relation sequence r_1...r_t define a derived historical context

q_t = (1-lambda) * sum_{k=1}^{t-1} lambda^(t-1-k) r_k.

q is not stored as an independent primitive. It is reconstructed from prior relation acts.

At the probe time, the present relation r_t is fixed to the same value across histories. A reversal request r'=-r_t is then applied.

The transition rule uses only the present relation and the derived relational context q_t. No label "memory" is given to q before measurement.

## Main criterion

Find pairs H_a, H_b such that:

1. present relation r_t is identical;
2. all external probe conditions are identical;
3. histories differ;
4. future transition probability or admissibility differs reproducibly.

If these conditions hold, the instantaneous relation is insufficient to predict the future. A history-derived relational state exists operationally.

## Controls

C1: identical histories, repeated probes.
C2: history permutation with identical present relation and identical total counts.
C3: lambda -> 0, removing historical dependence.
C4: randomized histories matched for present relation.

## Metrics

M1: variance of future response at fixed present relation.
M2: effect size between matched history classes.
M3: disappearance of the effect under lambda -> 0.
M4: predictive gain of q over present relation alone.

## Falsification

The hypothesis fails if matched histories produce no reproducible future difference, or if the effect survives after the historical term is removed.

## Important distinction

A positive result does not prove that memory is fundamental. It establishes only that a future-relevant relational state can be derived from prior relations.
