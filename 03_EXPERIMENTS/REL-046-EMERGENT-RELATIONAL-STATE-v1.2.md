# REL-046: Emergent relational state v1.2

Date: 2026-09-07
Status: EXPERIMENT_READY

This version fixes the transition rule before execution.

## Derived context

q_t(lambda) = sum_{j=1}^{t-1} lambda^j r_{t-j}, 0 < lambda < 1.

History-removal control: q_t = 0 exactly.

## Probe rule

Present relation r_t is fixed. A reversal request r'=-r_t is presented.

Probability of accepting the reversal:

p_rev = 1 / (1 + exp(k q_t r_t))

with k=5.

Thus positive historical alignment with the present relation increases resistance to reversal, while opposite historical support decreases resistance.

The probe itself is identical for matched histories.

## Test design

Primary pair:

H_A = [+1,+1,+1,-1,-1,+1]
H_B = [-1,-1,+1,+1,+1,+1]

Both have the same present relation (+1) and the same counts of prior +1 and -1 acts, but their ordering differs.

For each history and each lambda in {0, 0.2, 0.5, 0.8}, run 10,000 independent reversal probes using seed 20260907.

Expected observation under the hypothesis: future response differs for matched histories when lambda>0, while the difference collapses toward zero in the q=0 control.

## Secondary exhaustive control

Enumerate all 2^7 histories ending in +1. Compare the distribution of p_rev for lambda=0 against lambda>0.

## Decision

PASS requires:

1. reproducible matched-history effect for lambda>0;
2. effect substantially reduced in q=0 control;
3. the present relation alone cannot predict the measured response distribution;
4. q provides predictive information beyond r_t.

This is a model-level test, not a claim about physical systems.
