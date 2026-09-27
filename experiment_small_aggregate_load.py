"""Finite toy check for the aggregate-load Komlos cover criterion.

This experiment verifies one explicit random family and one explicit 3-coloring.
The proof of the general criterion is in Section 18.6 of the audit.
"""
from fractions import Fraction
import random

SEED = 20260923
M = 16
UNIVERSE_SIZE = 16_384
SUPPORT_SIZE = 4_096

rng = random.Random(SEED)
supports = [set(rng.sample(range(UNIVERSE_SIZE), SUPPORT_SIZE)) for _ in range(M)]
loads = [0] * UNIVERSE_SIZE
for support in supports:
    for z in support:
        loads[z] += 1

max_overlap = max(loads)
delta_upper = Fraction(M, SUPPORT_SIZE * SUPPORT_SIZE) ** Fraction(1, 2)
# Avoid irrational arithmetic for the criterion: max_overlap / SUPPORT_SIZE^2 < 1/468^2.
assert max_overlap <= M
assert M * 468**2 < SUPPORT_SIZE**2

colors = [rng.randrange(3) for _ in range(UNIVERSE_SIZE)]
counts = []
for support in supports:
    row = [sum(colors[z] == c for z in support) for c in range(3)]
    counts.append(row)
    assert max(row) * 2 < SUPPORT_SIZE, row

# A=0, B=1, C=2. The pair E=A union B and H=B union C
# has intersection B; confirm the strict-majority violation exactly.
for row in counts:
    a, b, c = row
    mass_e = Fraction(a + b, SUPPORT_SIZE)
    mass_h = Fraction(b + c, SUPPORT_SIZE)
    mass_intersection = Fraction(b, SUPPORT_SIZE)
    assert mass_e > Fraction(1, 2)
    assert mass_h > Fraction(1, 2)
    assert mass_intersection < Fraction(1, 2)

print(f"seed={SEED}; measures={M}; universe={UNIVERSE_SIZE}; support={SUPPORT_SIZE}")
print(f"max_point_overlap={max_overlap}; delta<=sqrt({M})/{SUPPORT_SIZE}={float(M**0.5 / SUPPORT_SIZE):.9f}")
print(f"criterion: {M}*468^2 < {SUPPORT_SIZE}^2 = {M * 468**2 < SUPPORT_SIZE**2}")
print(f"all 3-part masses strictly below 1/2: {len(counts)} / {M}")
print(f"cover pair verified exactly with Fraction arithmetic: {len(counts)} / {M}")
print(f"first_measure_part_counts={counts[0]}")
