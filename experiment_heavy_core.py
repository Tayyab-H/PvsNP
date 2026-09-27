"""Exact check of the shared-heavy-core / diffuse-tail cover criterion."""
from fractions import Fraction
from math import sqrt, pi
from random import Random

anchor_count = 3
heavy_atoms_per_anchor = 5
heavy_weight_per_atom = Fraction(1, 10)
tail_size = 100
tail_weight_per_atom = Fraction(1, 200)
core_mass = heavy_atoms_per_anchor * heavy_weight_per_atom
assert core_mass == Fraction(1, 2)
assert tail_size * tail_weight_per_atom == Fraction(1, 2)
assert 0 < core_mass <= Fraction(1, 2)

# Each anchor has four private heavy atoms; all measures share the diffuse tail.
cores = [set(range(a * heavy_atoms_per_anchor, (a + 1) * heavy_atoms_per_anchor)) for a in range(anchor_count)]
tail = set(range(anchor_count * heavy_atoms_per_anchor, anchor_count * heavy_atoms_per_anchor + tail_size))
universe = set().union(*cores, tail)

# The aggregate atom-norm cutoff theta=1/100 separates the private core atoms
# (weight 1/10 in one measure) from shared tail atoms (sqrt(3)/200).
theta = Fraction(1, 100)
assert Fraction(1, 10) > theta
assert sqrt(anchor_count) / 200 < float(theta)  # sqrt(3) < 2 gives the exact strict bound.
assert all(len(core) * heavy_weight_per_atom == Fraction(1, 2) for core in cores)

# Each tail point has normalized weight (1/200)/(1/2)=1/100
# in all three coordinates. Thus R=sqrt(3)/100.
R = Fraction(1, 100) * sqrt(anchor_count)
K = 3 * sqrt(2 * pi)
# Exact check using the ECCC constant 36: sqrt(3) < 2 gives 36 R < 72/100 < 1.
assert Fraction(36 * 2, 100) < 1
assert K * R < 1

rng = Random(20260923)
for trial in range(1, 10001):
    signs = {z: (1 if rng.getrandbits(1) else -1) for z in tail}
    discrepancy = tail_weight_per_atom * sum(signs.values())
    if abs(discrepancy) < core_mass:
        break
else:
    raise AssertionError("No tail signing found in 10,000 trials")

E = set().union(*cores, {z for z in tail if signs[z] == 1})
H = set().union(*cores, {z for z in tail if signs[z] == -1})
assert E & H == set().union(*cores)
for a, core in enumerate(cores):
    def mass(part):
        return len(core & part) * heavy_weight_per_atom + len(tail & part) * tail_weight_per_atom
    mE = mass(E)
    mH = mass(H)
    mI = mass(E & H)
    assert mE > Fraction(1, 2)
    assert mH > Fraction(1, 2)
    assert mI == core_mass <= Fraction(1, 2)

print(f"anchors={anchor_count}; heavy atoms per anchor={heavy_atoms_per_anchor}; shared tail={tail_size}")
print(f"aggregate cutoff theta=1/100 separates core atom norm 1/10 from tail atom norm sqrt(3)/200")
print(f"core mass per measure={core_mass}; tail mass=1/2; normalized radius=sqrt(3)/100={float(R):.8f}")
print(f"K=3sqrt(2pi)={K:.8f}; K*R={K*float(R):.8f} < 1")
print(f"ECCC K=36; exact bound 36R < 72/100 < 1")
print(f"found a valid partition on trial {trial}; for every measure E,H>1/2 and intersection=1/2")


