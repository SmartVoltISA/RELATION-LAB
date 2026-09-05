# RELATION-DISCOVERY-003 — Reconstruct Structure From Response Ensemble

**Status:** FAIL / informative negative result

## Question

Can observable intervention-response fingerprints reconstruct the latent spatial structure of a continuous medium when the estimator is given no spatial ordering, no distance metric, and no interaction matrix?

## Locked setup

- N = 40 continuous nonlinear elements.
- True dynamics: periodic ring, but the estimator observes a randomly permuted element labeling.
- Local background: nearest neighbours 0.10 each; second neighbours 0.035 each.
- Hidden relation: physical source 11 → physical target 31, K = +0.015.
- T = 4500.
- 60 intervention times.
- Intervention amplitude +0.5.
- Response horizon = 8 steps.
- 1560 ordered source-target pairs.
- The estimator receives only intervention-response fingerprints. No spatial ordering or hidden edge list is supplied.

## Blind representation

For each observed source, its complete 8-step response to all other observed targets was concatenated into a source-response fingerprint. Pair fingerprints were then represented by their 8-step temporal response vectors.

A spectral embedding was also computed from pairwise similarity between complete source-response fingerprints, as an attempt to reconstruct latent structure without using the true permutation.

The observed labels of the hidden relation were:

- physical source 11 → observed source **10**
- physical target 31 → observed target **16**

## Main result

The hidden pair did produce a reproducible response fingerprint, but unsupervised low-rank residual detection did not isolate it reliably.

| PCA background rank | ROC-AUC | Average Precision |
|---:|---:|---:|
| 1 | 0.0436 | 0.000670 |
| 2 | 0.7530 | 0.002591 |
| 3 | **0.7986** | **0.003175** |
| 4 | 0.7646 | 0.002717 |
| 5 | 0.7806 | 0.002915 |

Baseline AP for one positive among 1560 pairs is 1/1560 = **0.0006410**.

Thus the response ensemble contains some information about atypical structure (AUC up to 0.7986), but the extreme class imbalance and strong ordinary local response structure prevent reliable identification of the single hidden relation.

## Hidden pair response

Observed hidden pair = **10 → 16**.

Its mean response fingerprint was:

| Lag | Response |
|---:|---:|
| 1 | 0.0000000000 |
| 2 | 0.0000000000 |
| 3 | 0.0000110796 |
| 4 | 0.0000454439 |
| 5 | 0.0001085008 |
| 6 | 0.0001996257 |
| 7 | 0.0003145585 |
| 8 | 0.0004475895 |

The delayed onset is consistent with propagation through the latent local medium plus the weak hidden coupling, but this pattern was not sufficient for blind pair identification.

## Interpretation

This experiment does **not** support the stronger claim that geometry can be reconstructed automatically from response fingerprints with the present estimator.

It does support a weaker and useful statement:

> The ensemble of intervention responses contains recoverable structural information even when explicit spatial ordering is hidden.

The best low-rank residual detector reached ROC-AUC 0.7986, well above chance, but AP remained only 0.003175. With one positive in 1560 candidates, this is nowhere near a useful discovery system.

The failure is therefore not simply "there is no information". Rather, the current representation does not separate three things sufficiently:

1. ordinary background propagation;
2. latent geometry/structural proximity;
3. the additional hidden relation.

## Decision

**FAIL for reliable blind reconstruction.**

No confirmation experiment was performed because the discovery stage did not produce a sufficiently reliable locked source-target prediction. This prevents false promotion of an exploratory anomaly into a confirmed discovery.

## Consequence for the relation hypothesis

The experiment strengthens the methodological distinction:

`response exists` ≠ `relation identified`.

A relation detector must explain the response relative to a learned background model, not merely rank response magnitude or generic anomaly.

## Next experiment

Use the intervention-response ensemble to learn a **directed propagation operator** rather than a generic low-rank reconstruction:

1. estimate which target responses can be predicted from other source-response fingerprints;
2. infer latent propagation directions;
3. reconstruct a sparse directed response network;
4. identify residual edges not explained by that network;
5. freeze the candidate relation;
6. independently intervene and confirm the complete response fingerprint.

The key test becomes whether **relation can be defined as an irreducible component of the response operator after the reproducible background dynamics have been learned**.
