# REL-046: Emergent relational state v1.1

Date: 2026-09-07
Status: DEFINED

## Question

Can a future-relevant state be recovered as a derived quantity from relation history, without inserting an explicit memory/object/agent node?

## Constraint

Fundamental alphabet: relation acts r in {-1,+1}. No memory bit, object identity, node state, or E_comp is supplied as a primitive.

## Derived context

At probe time t, define

q_t(lambda) = sum_{j=1}^{t-1} lambda^j r_{t-j},  0 < lambda < 1.

For the history-removal control, q_t is set exactly to 0. Therefore C3 contains no historical contribution.

q is reconstructed from prior relation acts and is not introduced as an independent state primitive.

The present relation r_t is fixed across histories. A reversal request r'=-r_t is then applied under identical external conditions.

Transition probability is a deterministic function of the present relation and q. The label "memory" is not used during the measurement.

## Main criterion

Find matched histories with identical present relation and probe conditions but different future response. Then remove q and verify that the effect disappears.

## Controls

C1: repeated probes of identical histories.
C2: history permutations with identical present relation and identical total counts.
C3: exact history removal q=0.
C4: randomized histories matched for present relation.

## Metrics

M1: response variance at fixed present relation.
M2: matched-history effect size.
M3: disappearance of the effect under q=0.
M4: predictive gain of q over present relation alone.

## Falsification

The hypothesis fails if matched histories do not alter future response, or if the effect remains when q=0.

## Interpretation boundary

A positive result establishes only that a future-relevant relational state can be derived from history. It does not establish that memory is fundamental.
