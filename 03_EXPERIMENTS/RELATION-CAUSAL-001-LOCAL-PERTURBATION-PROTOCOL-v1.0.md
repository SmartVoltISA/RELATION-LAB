# RELATION-CAUSAL-001 — Local perturbation and propagation recovery

**Status:** PROTOCOL LOCKED / EXECUTION PENDING
**Date:** 2026-09-05

## Purpose

Test whether a relation can be recovered more cleanly from the system's response to a controlled local perturbation than from passive pairwise correlation.

## Research question

Given a continuous spatial medium with many correlated elements, can a localized intervention at element `i` reveal the direct relation `i -> j` from the differential response, while separating direct, indirect, common-cause and noise effects?

## Ground-truth model

Use a periodic 1D field with `N=40` continuous elements. Dynamics:

`X[t+1] = 0.70 X[t] + 0.08 L X[t] + u[t] + eps[t]`

where `L` contains known local nearest-neighbour and second-neighbour couplings. One hidden target edge `10 -> 11` is added with time-varying coefficient:

| Time | True K(11,10) |
|---:|---:|
| 0–999 | 0.00 |
| 1000–1999 | +0.18 |
| 2000–2999 | +0.05 |
| 3000–3999 | 0.00 |
| 4000–4999 | −0.16 |

Noise is zero-mean Gaussian and independent between elements.

## Intervention

At predetermined times, create paired trajectories from identical pre-intervention states and identical future noise streams:

- control: no perturbation;
- intervention: `X_10 <- X_10 + delta`, with `delta=1.0`.

Do not reveal the target edge to the estimator. Estimate the response field:

`R_j(tau) = E[X_j(t0+tau | do(X_10+=delta)) - X_j(t0+tau | control)]`.

## Direct-effect criterion

A candidate direct relation `10 -> j` must satisfy all of:

1. response appears at the first dynamically permitted lag;
2. response amplitude scales approximately linearly with `delta` for small perturbations;
3. response is reproducible over independent seeds;
4. response disappears under source permutation;
5. target response exceeds an appropriate indirect-path null after controlling for intermediate nodes;
6. sign of the response agrees with the hidden coupling where coupling is nonzero.

## Required controls

- no-intervention control;
- source-index permutation;
- time-shuffled trajectories;
- independent random seeds;
- positive/negative perturbations `delta=+1,-1`;
- perturbation magnitudes `0.5,1.0,2.0`;
- stationary-coupling baseline;
- nonlocal/random-coupling control.

## Required result table

`source | target | true K | lag | observed response | normalized response | sign | seed SD | permutation percentile | direct/indirect classification`

## Decision rule

A causal-relation recovery claim requires reproducible separation from permutation/time-shuffle controls across independent seeds and perturbation magnitudes. A response alone is not sufficient: propagation through an indirect path must not be mistaken for a direct relation.

## Important boundary

This experiment tests operational causal recoverability in a specified continuous dynamical medium. It does not establish that `K` is ontologically fundamental or that physical relations in nature must have this representation.

## Next execution

Run the locked protocol and record the full numerical response table before interpreting the result. If the perturbation experiment succeeds where passive recovery fails, compare the two methods directly; if it fails, preserve the failure as evidence against this operational definition.
