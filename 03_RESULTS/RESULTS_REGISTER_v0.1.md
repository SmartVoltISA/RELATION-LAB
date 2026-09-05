# Results register v0.1

| ID | Experiment | Result | Status | Limitation |
|---|---|---|---|---|
| REL-EXP-001 | Time-varying relation | K_AB(t) recovered with MAE 0.024 | SUPPORTED IN MODEL | Synthetic, controlled system |
| REL-EXP-002 | Continuous-like field | Structure recovered above shuffled control; ROC-AUC 0.7548 | PARTIAL | Correlated states reduce accuracy |
| REL-CTRL-001 | Time-shuffled control | Temporal relation signal largely disappears | CONTROL PASSED | Control is model-specific |
| REL-OBS-001 | Direct vs indirect/common-cause models | Observed dependence does not uniquely identify direct relation | SUPPORTED | Synthetic models |
| REL-INT-001 | Controlled intervention model | Direct effects recovered under intervention | SUPPORTED IN MODEL | Requires correct intervention assumptions |

## Evidence policy

A result enters this register only after execution. Proposed experiments remain in hypotheses/protocols and are not counted as results.

## Current state

The strongest present statement is operational:

> In tested synthetic dynamical systems, relational influence can be represented and partially recovered as a state-transition dependency, including time variation and sign changes.

No physical or ontological claim is established by these experiments alone.
