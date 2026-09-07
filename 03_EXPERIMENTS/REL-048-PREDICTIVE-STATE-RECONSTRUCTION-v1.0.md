# REL-048: Predictive State Reconstruction v1.0

Date: 2026-09-07
Status: EXPERIMENT_DESIGN

## Question

Can an effective state be recovered from a restricted observation of a relational dynamical system without inserting an explicit memory variable?

## Principle

Do not define q, memory, history strength, or a hidden state in the generator.
The generator contains only local relational variables and a deterministic local update rule.

The observer sees only a restricted observable O(X), not the complete configuration X.

## Model

Use a ring of N=16 binary relation acts r_i in {-1,+1}.

At each tick every relation is updated synchronously from its local triplet:

r_i(t+1) = sign(r_{i-1}(t) + r_i(t) + r_{i+1}(t))

For a zero sum, retain r_i(t). This is a local majority rule with no explicit history term.

No agent, node memory, hidden variable, or externally supplied state is added.

## Observation map

For a selected center relation c, the observer receives only:

O(X_t) = r_c(t)

The surrounding relational configuration is unobserved.

## Reconstruction

Generate many trajectories from randomized initial relational configurations.
For each observed history h_t=(O(X_0),...,O(X_t)), estimate the empirical distribution of the next observation O(X_{t+1}).

Histories are placed in the same predictive class when their next-observation distributions are statistically indistinguishable within preregistered tolerance epsilon.

Increase history length L until predictive distributions stabilize on held-out trajectories.

The recovered class is an effective state only if:

1. it predicts held-out future observations better than the instantaneous observation alone;
2. the partition is reproducible across independent trajectory sets;
3. the number of classes stabilizes rather than growing with sample size;
4. no explicit memory variable is used by the generator;
5. the class corresponds to persistent relational configurations when the full system is inspected after the analysis is locked.

## Controls

C1: shuffled observation histories preserving marginal symbol frequencies.
C2: independent random relation updates with the same marginal transition frequencies.
C3: full-state predictor using X_t, establishing the upper reference bound.
C4: observation of a second center relation, testing whether predictive power depends on observation choice.

## Metrics

M1: held-out log loss of instantaneous observation predictor.
M2: held-out log loss of reconstructed-state predictor.
M3: predictive gain Delta = M1 - M2.
M4: number of recovered predictive classes.
M5: cross-seed partition agreement.
M6: persistence of relational structure associated with each recovered class.

## Falsification

The experiment does not support emergent effective state if predictive gain vanishes, partitions fail to reproduce, or classes simply encode finite-history labels without stable predictive behavior.

A positive result establishes only an effective predictive state relative to O. It does not establish fundamental memory.

## Required execution

All runs must be local and deterministic with recorded seeds. No GitHub Actions execution is assumed.

Before execution, code and parameters must be frozen. Results must be written separately from the protocol.
