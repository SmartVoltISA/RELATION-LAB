"""REL-048 local reference implementation.

No explicit memory variable is used by the generator. The only generator
state is the current 16-cell binary relational configuration.
"""

from __future__ import annotations
import math
import random
from collections import defaultdict

N = 16
STEPS = 40
SEEDS = 5000
L = 6


def majority(a: int, b: int, c: int) -> int:
    s = a + b + c
    return b if s == 0 else (1 if s > 0 else -1)


def step(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(majority(x[(i-1) % N], x[i], x[(i+1) % N]) for i in range(N))


def trajectory(seed: int):
    rng = random.Random(seed)
    x = tuple(rng.choice((-1, 1)) for _ in range(N))
    obs = []
    for _ in range(STEPS + L):
        obs.append(x[0])
        x = step(x)
    return tuple(obs)


def log_loss(p: float, y: int) -> float:
    p = min(max(p, 1e-12), 1 - 1e-12)
    return -math.log(p if y == 1 else 1 - p)


# Build samples from independent trajectories.
train = [trajectory(s) for s in range(SEEDS)]
test = [trajectory(100000 + s) for s in range(SEEDS // 2)]

# Instantaneous predictor: P(next | current observation).
counts0 = defaultdict(lambda: [0, 0])
for tr in train:
    for t in range(len(tr) - 1):
        counts0[tr[t]][0 if tr[t+1] == -1 else 1] += 1
p0 = {k: (v[1] + 0.5) / (sum(v) + 1.0) for k, v in counts0.items()}

# History reconstruction: empirical predictive distribution for each exact
# observed history of length L. This is a reconstruction from observations,
# not a generator-side state variable.
counts = defaultdict(lambda: [0, 0])
for tr in train:
    for t in range(L - 1, len(tr) - 1):
        h = tr[t-L+1:t+1]
        counts[h][0 if tr[t+1] == -1 else 1] += 1

ph = {h: (v[1] + 0.5) / (sum(v) + 1.0) for h, v in counts.items()}

ll0 = []
llh = []
for tr in test:
    for t in range(L - 1, len(tr) - 1):
        ll0.append(log_loss(p0[tr[t]], tr[t+1]))
        h = tr[t-L+1:t+1]
        p = ph.get(h, p0[tr[t]])
        llh.append(log_loss(p, tr[t+1]))

print(f"N={N} STEPS={STEPS} TRAIN={len(train)} TEST={len(test)} L={L}")
print(f"instantaneous_logloss={sum(ll0)/len(ll0):.8f}")
print(f"history_logloss={sum(llh)/len(llh):.8f}")
print(f"predictive_gain={sum(ll0)/len(ll0)-sum(llh)/len(llh):.8f}")
print(f"recovered_history_classes={len(ph)}")
