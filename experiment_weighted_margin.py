"""Exact finite sanity check for the weighted-margin discrepancy criterion."""
from itertools import combinations
from math import comb, pi, sqrt
from random import Random

N = 16
all_ones = (1 << N) - 1

# Radius-two supports around 0^N and 1^N; the two supports are disjoint.
support_zero = {0}
for weight in (1, 2):
    for positions in combinations(range(N), weight):
        support_zero.add(sum(1 << i for i in positions))
support_one = {all_ones ^ z for z in support_zero}
universe = sorted(support_zero | support_one)

support_size = 1 + N + comb(N, 2)
flips_at_each_coordinate = 1 + (N - 1)
margin_numerator = support_size - 2 * flips_at_each_coordinate
assert len(support_zero) == len(support_one) == support_size == 137
assert support_zero.isdisjoint(support_one)
assert margin_numerator == 105

# For a point in one support, there are N normalized coordinates of
# magnitude 1/105 and zeros in the other anchor block. Hence R=4/105.
normalized_radius = sqrt(N) / margin_numerator
komlos_constant = 3 * sqrt(2 * pi)
assert komlos_constant * normalized_radius < 1

rng = Random(20260923)
for trial in range(1, 10001):
    signs = {z: (1 if rng.getrandbits(1) else -1) for z in universe}
    valid = True
    for support, anchor in ((support_zero, 0), (support_one, all_ones)):
        for coordinate in range(N):
            signed_margin = sum(
                signs[z]
                * (
                    1
                    if ((z >> coordinate) & 1) == ((anchor >> coordinate) & 1)
                    else -1
                )
                for z in support
            )
            if abs(signed_margin) >= margin_numerator:
                valid = False
                break
        if not valid:
            break
    if valid:
        break
else:
    raise AssertionError("No valid partition found in 10,000 trials")

# Verify all side-wise strict majorities using integer counts.
for support, anchor in ((support_zero, 0), (support_one, all_ones)):
    for coordinate in range(N):
        for side in (1, -1):
            side_points = [z for z in support if signs[z] == side]
            matches = sum(
                ((z >> coordinate) & 1) == ((anchor >> coordinate) & 1)
                for z in side_points
            )
            assert 2 * matches > len(side_points)

print(f"N={N}; universe={len(universe)}; support per anchor={support_size}")
print(f"exact signed margin={margin_numerator}/{support_size}")
print(f"normalized column radius=sqrt({N})/{margin_numerator}={normalized_radius:.8f}")
print(f"K=3sqrt(2pi)={komlos_constant:.8f}; K*R={komlos_constant * normalized_radius:.8f} < 1")
print(f"valid partition found on trial {trial}; all {2 * N} anchor-coordinate majorities verified")
