# RELATION-INVAR-002 — Resolution Scaling Result v1.0

## Status
**EXECUTED / NUMERICAL RESULT**

## Question
Does an operational relation survive a change of spatial resolution, or is it only an artifact of the chosen node decomposition?

## Model
N = 40 fine elements on a periodic 1D medium. Hidden directed relation 10 -> 12 has time-varying coefficient K:

| Segment | K |
|---:|---:|
| 0–999 | 0.00 |
| 1000–1999 | +0.18 |
| 2000–2999 | +0.05 |
| 3000–3999 | 0.00 |
| 4000–4999 | −0.16 |

Dynamics contain background nearest- and second-neighbour coupling and stochastic forcing. A paired intervention X10 += 1 was applied with identical future noise.

## Resolution transformation
Fine variables were coarse-grained by averaging consecutive blocks of size b = 1, 2, 4, 5, 8, 10.

The hidden edge was deliberately changed to 10 -> 12 so that at b <= 4 source and target remain in distinct coarse cells. At b >= 5 they can merge into the same coarse cell; this is an intentional resolution-loss test.

## Numerical result: lag 1 target response

| Block size b | K=0 | K=+0.18 | K=+0.05 | K=0 | K=-0.16 |
|---:|---:|---:|---:|---:|---:|
| 1 | +0.001225 | +0.007525 | +0.002975 | +0.001225 | −0.004375 |
| 2 | +0.000613 | +0.003763 | +0.001488 | +0.000613 | −0.002188 |
| 4 | +0.000306 | +0.001881 | +0.000744 | +0.000306 | −0.001094 |
| 5 | +0.197445 | +0.198705 | +0.197795 | +0.197445 | +0.196325 |
| 8 | +0.123994 | +0.124781 | +0.124212 | +0.123994 | +0.123294 |
| 10 | +0.098722 | +0.099352 | +0.098898 | +0.098722 | +0.098163 |

For b=1,2,4 the incremental relation signal above the K=0 baseline is:

| b | Δ response for K=+0.18 | Expected scaling |
|---:|---:|---:|
| 1 | +0.006300 | +0.006300 |
| 2 | +0.003150 | +0.003150 |
| 4 | +0.001575 | +0.001575 |

Thus coarse-graining preserves the sign and relative state dependence while the averaged response magnitude scales approximately as 1/b, as expected from block averaging.

## Resolution failure / merging
At b=5, source 10 and target 12 fall into the same coarse cell. The measured target-cell response becomes dominated by the source perturbation itself (~0.197), and the hidden K-dependent increment is no longer separable from the within-cell response.

At b=8 and b=10 the same effect persists: the coarse variable contains both source and target, so the original directed pairwise relation is not identifiable from that coarse variable alone.

## Interpretation
The experiment gives a two-part result.

1. **Representation robustness:** while source and target remain separately resolved, the operational relation survives coarse-graining. Its numerical coefficient changes with resolution, but the signed incremental response and its dependence on K remain.
2. **Resolution boundary:** once source and target are merged into one observed variable, the directed relation is lost as a separately identifiable object. This is not a failure of the relation itself; it is an information-loss boundary of the measurement representation.

Therefore the strongest current statement is:

> Relation is more robust than its scalar coefficient, but recoverability requires sufficient resolution to distinguish the participating degrees of freedom.

## What this establishes
- A relation measurement need not be invariant as a number under coarse-graining.
- The qualitative/direct-response structure can survive a change of resolution when source and target remain distinguishable.
- Coarse-graining can destroy identifiability by merging the source and target into one observed degree of freedom.
- Therefore a universal relation theory must specify the resolution/observability conditions under which a relation is defined.

## What this does NOT establish
- It does not prove that relation is ontologically fundamental.
- It does not prove resolution-independent existence of a particular pairwise edge.
- It does not establish that physical systems have a preferred minimum resolution.
- It does not prove that a continuum relation kernel is uniquely recoverable from finite-resolution observations.

## Decision
**PASS — partial invariance, with an explicit information-loss boundary.**

## Next test
Test temporal coarse-graining and mixed spatial-temporal coarse-graining. Then test whether the relation can be represented as an invariant operator/response class rather than a scalar coefficient, and whether that object survives both coordinate transformation and resolution changes simultaneously.
