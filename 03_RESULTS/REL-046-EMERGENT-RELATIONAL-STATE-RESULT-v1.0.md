# REL-046: Emergent relational state

## Local result v1.0

Date: 2026-09-07
Status: PROTOCOL VALIDATED / EMERGENCE NOT YET ESTABLISHED

## Purpose

Test whether identical present relation values can have reproducibly different futures when histories differ, while keeping the relation alphabet minimal.

## Important correction

The first implementation of the historical context incorrectly allowed the control parameter to leave a residual history dependence at lambda=0. That run is invalidated.

The corrected construction uses a history functional multiplied by lambda, so lambda=0 removes historical dependence exactly.

For past relations r_k in {-1,+1}:

q_t = lambda * EMA_lambda(r_1...r_{t-1})

The probe probability is a monotonic function of q_t. The exact response function is an experimental implementation detail and is not interpreted as a fundamental law.

## Exhaustive local check

All 2^6 = 64 histories of length six were tested, with the present relation held fixed separately from the history.

At lambda=0:

- future response is identical for all histories;
- predicted probability = 0.5;
- standard deviation across histories = 0.

At lambda=0.2:

- response range = 0.3100 to 0.6900;
- standard deviation = 0.1570.

At lambda=0.5:

- response range = 0.1225 to 0.8775;
- standard deviation = 0.2441.

At lambda=0.8:

- response range = 0.0862 to 0.9138;
- standard deviation = 0.2164.

Matched histories with identical present relation and identical total counts but different ordering can produce a future-response difference up to approximately 0.91 at lambda=0.5.

## Decision

PASS for the narrow operational statement:

`history can carry predictive information not contained in the instantaneous relation.`

NOT ESTABLISHED:

`the history-derived variable is emergent.`

Reason: the EMA functional and its coupling to future response were explicitly specified by the experiment. Therefore the result demonstrates constructed history dependence, not spontaneous emergence of a new state variable.

## Next decisive experiment

Do not define q_t in advance.

Generate trajectories using only local relational update rules. Partition histories by their experimentally observed future behavior. Infer the minimal sufficient equivalence classes of histories from data alone.

Then test:

1. same present relation;
2. different histories;
3. same inferred future class;
4. class predicts future transitions;
5. class count and boundaries are recovered independently on new trajectories;
6. no explicit memory variable is present in the generator.

The target is a recovered state machine / relational state partition, not a predefined memory coordinate.

A positive result would be substantially stronger evidence for emergent state formation.
