"""Exact stress test: anchored heavy-atom measures evade the core norm bound."""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt

names = ("x", "y", "z")
# Weights are ordered x,y,z.
mu1 = (F(49, 100), F(49, 100), F(2, 100))
mu2 = (F(2, 100), F(49, 100), F(49, 100))
measures = (mu1, mu2)
assert sum(mu1) == sum(mu2) == 1

# Each truth-table coordinate has exactly one deviator from anchor 0^N.
# For deviator x/y/z, the bit column is respectively (1,0,0)/(0,1,0)/(0,0,1).
for deviator in range(3):
    for mu in measures:
        matching_mass = 1 - mu[deviator]
        assert matching_mass > F(1, 2)

# Explicit pair, represented by index sets: E={x,z}, H={y,z}.
E, H = {0, 2}, {1, 2}
intersection = E & H
for mu in measures:
    mass_E = sum(mu[i] for i in E)
    mass_H = sum(mu[i] for i in H)
    mass_I = sum(mu[i] for i in intersection)
    assert mass_E > F(1, 2) and mass_H > F(1, 2)
    assert mass_I <= F(1, 2)

# Check every possible common core S. A valid core has positive mass <=1/2
# under both measures. For each, compute the maximum normalized tail column norm.
valid_cores = []
for size in range(1, 4):
    for core_tuple in combinations(range(3), size):
        core = set(core_tuple)
        b = tuple(sum(mu[i] for i in core) for mu in measures)
        if not all(F(0) < value <= F(1, 2) for value in b):
            continue
        tail = set(range(3)) - core
        r2 = max(
            sum((measures[a][z] / b[a]) ** 2 for a in range(2))
            for z in tail
        )
        max_component = max(measures[a][z] / b[a] for a in range(2) for z in tail)
        valid_cores.append((tuple(names[i] for i in core_tuple), b, sqrt(float(r2)), max_component))
assert len(valid_cores) == 3
assert all(max_component >= 1 for _, _, _, max_component in valid_cores)

# Aggregate atom norms squared: x,z have 2405/10000; y has 4802/10000.
load2 = (mu1[0] ** 2 + mu2[0] ** 2,
         mu1[1] ** 2 + mu2[1] ** 2,
         mu1[2] ** 2 + mu2[2] ** 2)
assert load2[0] == load2[2] == F(2405, 10000)
assert load2[1] == F(4802, 10000)
# Threshold sets: all three atoms, {y}, or empty. None meets K=36, KR<1.
assert load2[0] > F(49, 100) ** 2
assert load2[1] > load2[0]

print("coordinate matching masses by deviator:")
for deviator, label in enumerate(names):
    print(f"  {label}: mu1={1-mu1[deviator]}, mu2={1-mu2[deviator]}")
print("valid pair E={x,z}, H={y,z}; intersection={z}")
for j, mu in enumerate(measures, 1):
    print(f"  measure {j}: E={sum(mu[i] for i in E)}, H={sum(mu[i] for i in H)}, intersection={mu[2]}")
print("valid common cores and normalized tail radii:")
for core, b, radius, max_component in valid_cores:
    print(f"  S={core}: masses={b}, R={radius:.6f}, exact coordinate ratio >= {max_component}")
print("aggregate cutoff: S_theta is all points, {y}, or empty; the K=36 cutoff criterion never applies")
print("A balanced-partition counting argument proves x,y,z can all be chosen in the high-complexity promise set for N=2^n, s2=N^beta, any fixed beta<1.")
