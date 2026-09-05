# Relation — operational definition v0.1

Status: WORKING DEFINITION / OPEN TO FALSIFICATION

## Question

What is a relation between two distinguishable elements A and B?

## Working definition

A relation is an experimentally detectable dependence of the state-transition behavior of one element on the state of another element.

For a system

`X(t+1) = F(X(t), t)`

a local directional relation can be represented by

`K_ji(t) = ∂F_j / ∂X_i`

where `K_ji` is an operational measure of how a change in element i changes the transition of element j.

## Important distinction

A relation is not automatically identical to:

- a graph edge;
- a force;
- a physical field;
- energy;
- causality;
- correlation;
- geometric proximity.

These are competing interpretations or mathematical representations to be tested.

## Observational hierarchy

1. Dependence: `P(Y|X) ≠ P(Y)`.
2. Predictive influence: `P(Y_next|Y,X) ≠ P(Y_next|Y)`.
3. Intervention effect: `P(Y|do(X=x1)) ≠ P(Y|do(X=x2))`.
4. Structural/local influence: estimate `K_ji` while controlling declared variables.

Higher levels require stronger assumptions and controls.

## Continuous extension

For a continuous field `X(r,t)`:

`X(t+1) = F[X(t), t]`

and a candidate relation kernel is

`K(r,r',t) = δF(r,t) / δX(r',t)`.

This is a candidate operational representation, not an ontological claim.

## Falsification target

The definition is weakened if observed transition behavior can be reproduced without dependence on the proposed source state, or if the measured effect disappears under appropriate controls.
