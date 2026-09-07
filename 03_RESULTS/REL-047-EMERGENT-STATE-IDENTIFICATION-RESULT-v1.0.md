# REL-047: Emergent State Identification v1.0

Date: 2026-09-07
Status: RESULT / SCOPE LIMIT

## Execution

A local deterministic relational cellular system was tested as a control for state reconstruction. Fundamental binary relation values were updated synchronously from the current relational configuration only. No explicit memory variable, history term, agent state, or hidden state variable was inserted.

A complete local configuration is therefore Markovian: X(t+1)=F(X(t)).

The experiment was used primarily to test the logical boundary of REL-046.

## Result 1: full state

For a deterministic generator, identical complete relational configurations necessarily produce identical next configurations. Therefore a genuinely history-dependent future cannot be demonstrated while the complete microstate is observed and the transition law is fixed.

This is an exact consequence of the model definition, not a failed numerical test.

## Result 2: coarse observation

When only a local relation r_c(t) is observed, different complete relational configurations can share the same observed relation while having different next responses. This reproduces the familiar same-present/different-future phenomenon, but the missing information is spatial relational context, not demonstrated memory.

## Result 3: interpretation

A predictive state can be recovered only relative to an observation map. If O(X) discards degrees of freedom, histories or observations may be grouped into effective predictive classes. Such a class is an emergent/effective state in the operational sense only after reconstruction and held-out validation. It must not be promoted to a fundamental memory variable without additional evidence.

## Consequence for REL-046

The previous q-based result remains valid only for the narrow statement that explicitly supplied history can alter future response. It does not establish emergence.

The decisive route is now clear:

1. choose a relational system with no explicit memory;
2. define a restricted observation O(X);
3. generate trajectories from local relational dynamics;
4. infer predictive equivalence classes from observations alone;
5. verify the classes on independent trajectories;
6. test whether the recovered class corresponds to a persistent relational structure rather than a predefined memory coordinate.

## Scientific status

NOT PROOF OF EMERGENT MEMORY.

SUPPORTED: instantaneous observed relation may be insufficient because relational context is hidden by coarse-graining.

SUPPORTED: a predictive state can, in principle, be an equivalence class over observations/history rather than a primitive variable.

NOT ESTABLISHED: that such a state is ontologically fundamental or that memory emerges without an underlying unobserved degree of freedom.

This result is a boundary condition for future Ω relational-state experiments.
