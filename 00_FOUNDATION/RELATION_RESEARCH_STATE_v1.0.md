# RELATION-LAB — Research State v1.0

Date: 2026-09-05
Status: ACTIVE RESEARCH

## What we can currently say

1. A relation can be treated operationally as a reproducible dependence of one state transition on another, provided controls distinguish it from indirect dependence, common cause and noise.
2. Directional influence can be recovered in controlled synthetic dynamical systems; intervention is stronger evidence than correlation alone.
3. A single instantaneous relation/change vector is not generally sufficient to determine the future: an exhaustive binary-rule analysis found 56/256 deterministic rules with at least one same-relation/different-next-relation ambiguity.
4. Relation classes can emerge from invariants and symmetry, but the number of observed relation values must not be equated with the number of fundamental relation types.
5. Memory can alter transition resistance in a controlled model: surgical deletion of stored memory reduced mean reversal delay from 2.626667 to 1.000000 steps in the registered experiment.
6. Minimal cellular media can generate localized propagating structures, but the electron hunt did not identify an electron.
7. Known electron numerical constants and derived quantities were independently reproduced; this is a verification of numerical consistency, not evidence for a new ontology.
8. Relation-first clustering of a supplied particle dataset found nonrandom structure, but because the features encoded known Standard Model categories it did not establish new physics.

## What remains unproven

- that relation is ontologically more fundamental than particles, fields, space or time;
- that all physical interaction is reducible to one universal relation variable;
- that relation has a universal scalar strength;
- that relation is necessarily symmetric or necessarily dual;
- that memory is universally a property of relation rather than state;
- that energy is universally identical to relation change;
- that a physical electron can emerge from a relation-only medium;
- that a continuous physical relation kernel K(r,r',t) can be recovered without presupposing the node decomposition.

## Strongest current mathematical bridge

For a state vector X(t):

`X(t+1) = F(X(t), t) + noise`

The local direct influence candidate is:

`K_ji(t) = ∂F_j/∂X_i`

For a continuous field:

`K(r,r',t) = δF(r,t)/δX(r',t)`

The key research task is to estimate these objects from observations, interventions and controls, then test whether the recovered structure is stable under changes of representation, resolution and coordinate choice.

## Next decisive experiment

A continuous analogue-like medium with a known time-varying coupling will be used as a hidden ground-truth system. The coupling will switch strength and sign over predetermined windows. The estimator must recover the change using only observed trajectories.

Required controls:

- time-shuffled data;
- spatial/source permutation;
- independent random seeds;
- simpler stationary model;
- nonlocal/random coupling control;
- multiple window sizes;
- held-out windows for final evaluation.

Required table columns:

`window | true K_ij | estimated K_ij | absolute error | sign correct | control score | seed variability`

No success claim is permitted until the table is produced from an executed run.

## Decision rule

If the estimator tracks the hidden coupling significantly better than the null and competing simpler models across independent seeds and window sizes, the operational relation concept is strengthened.

If it fails, the failure remains a result and the representation or definition must be revised.
