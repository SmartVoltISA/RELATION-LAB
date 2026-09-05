# RELATION-FUNDAMENTAL-010 — Element, State, Relation Recovery Without Predefined Elements

Date: 2026-09-05
Status: COMPLETE EXPERIMENT — PARTIAL PASS

## Question

Can distinguishable elements, their dynamical states, and relations be recovered from observations when the observer is not given the original element decomposition or coordinate system?

## Locked model

A 5-dimensional stable latent dynamical system was generated with directed transition structure. The observer did not receive the latent variables or the generating matrix.

The latent state was observed through 80 dense, unknown linear mixtures plus measurement noise. Thus the observed coordinates were not the true elements and had no privileged one-to-one interpretation.

T = 6000 observations.
Latent dimension = 5.
Observed dimension = 80.

True latent transition matrix eigenvalues:

`0.79334, 0.70892 ± 0.10434i, 0.56941 ± 0.06287i`

## A. Recovering distinguishable dynamical dimensions

Singular-value decomposition of the observation covariance was used without knowledge of the latent dimension.

| Retained dimensions | One-step latent reconstruction MSE |
|---:|---:|
| 3 | 0.0077049 |
| 4 | 0.0078739 |
| 5 | 0.0076839 |
| 8 | 0.0052060 |
| 10 | 0.0043776 |

The first five principal directions captured the dominant stable dynamical subspace, but additional observed dimensions continued to capture measurement/noise structure.

## B. Recovering dynamics up to representation

A VAR(1) operator was fitted in the recovered 5-dimensional subspace.

Recovered eigenvalues:

`0.75290, 0.66177 ± 0.08283i, 0.51246 ± 0.06321i`

The ordering and damping structure were preserved, but the numerical eigenvalues were biased by finite observation noise and imperfect subspace recovery.

This is an important negative result: blind recovery does not reproduce the generating operator exactly from noisy observations.

## C. Invariance under a second unknown observation mixing

The same physical latent process was passed through a different dense invertible 80×80 observation transformation before repeating the blind recovery.

Recovered eigenvalues:

`0.68327, 0.61377 ± 0.07383i, 0.46975 ± 0.04374i`

The numerical latent coordinates changed substantially. The qualitative dynamical mode structure remained: five dominant modes with the same ordering of slow/fast decay and oscillatory/non-oscillatory character.

## D. What was and was not recovered

| Object | Recovery status |
|---|---|
| Number of dominant dynamical degrees of freedom | approximately recovered |
| Individual original latent variables | not uniquely recovered |
| Original matrix entries | not invariant / not recovered |
| Dynamical mode spectrum | qualitatively recovered |
| Physical input-output predictions | representation-dependent observation map required |
| Pairwise graph edges in latent coordinates | not uniquely identifiable |
| Dynamical subspace | recovered approximately |

## E. Key result

The experiment separates three levels that were previously conflated:

1. The observer can recover a set of distinguishable dynamical degrees of freedom from raw temporal behavior.
2. The particular decomposition into elements is not unique.
3. The numerical relation matrix between those recovered coordinates is therefore not unique either.

The invariant candidate is not the identity of a particular latent element and not a particular matrix edge. It is the equivalence class of dynamical behavior that remains predictive under a change of representation.

## F. Interpretation

This is a PARTIAL PASS, not a full proof.

The experiment supports:

`raw dynamics → distinguishable dynamical subspace → state representation → relational operator`

but it does not establish unique recovery of the original elements or relations.

This is exactly what should happen if elements are modeling choices rather than ontological primitives.

The strongest surviving candidate is therefore a representation-equivalence class of response operators rather than a unique list of fundamental nodes and edges.

## G. Updated hypothesis

A physically meaningful relation should be expected to survive as an invariant prediction or response class under admissible changes of representation, even when the individual elements used to express that relation change.

This is weaker and more defensible than requiring a unique pairwise relation matrix.

## H. Remaining decisive tests

1. Repeat with nonlinear unknown observation maps rather than dense linear mixtures.
2. Repeat with stochastic latent dynamics and state-dependent relations.
3. Test whether intervention-equivalent response classes can be recovered without knowing the true latent variables.
4. Test whether two different decompositions can be proven observationally equivalent while assigning different pairwise relations.
5. Extend to field-like systems where the decomposition into elements is continuously variable.

## Final conclusion

**PARTIAL PASS.**

The experiment does not show that elements are fundamental. It shows the opposite possibility is viable: observable dynamics can contain enough structure to recover distinguishable dynamical degrees of freedom without a predefined element list, while the detailed identity of elements and pairwise coefficients remains non-unique.

Therefore the present evidence favors a hierarchy in which **dynamical response structure is more invariant than the particular elements used to represent it**.
