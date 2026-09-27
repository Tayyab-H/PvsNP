"""Exact search for the best recursive binary-split cover threshold.

Each split uses a Komlos signing with k = K*delta, giving a depth-d leaf
upper bound 2**(-d) + (1 - 2**(-d))*k. This searches every full binary
split-tree depth multiset with at most seven leaves and every 3-way grouping.
"""
from fractions import Fraction
from itertools import product


def all_depth_multisets(max_leaves):
    found = {(0,)}
    frontier = {(0,)}
    while frontier:
        new = set()
        for depths in frontier:
            if len(depths) >= max_leaves:
                continue
            for i, depth in enumerate(depths):
                child = tuple(sorted(depths[:i] + depths[i + 1:] + (depth + 1, depth + 1)))
                new.add(child)
        new -= found
        found |= new
        frontier = new
    return found


def best_threshold(depths):
    m = len(depths)
    base = [Fraction(1, 2**d) for d in depths]
    error = [1 - x for x in base]
    best = Fraction(0)
    for assignment in product(range(3), repeat=m):
        if len(set(assignment)) != 3:
            continue
        ratios = []
        for color in range(3):
            mass = sum((base[i] for i, c in enumerate(assignment) if c == color), Fraction())
            coefficient = sum((error[i] for i, c in enumerate(assignment) if c == color), Fraction())
            if mass >= Fraction(1, 2):
                break
            ratios.append((Fraction(1, 2) - mass) / coefficient)
        else:
            best = max(best, min(ratios))
    return best


trees = all_depth_multisets(7)
expected = {
    3: Fraction(0),
    4: Fraction(0),
    5: Fraction(1, 13),
    6: Fraction(1, 13),
    7: Fraction(1, 13),
}
for leaves, target in expected.items():
    values = [best_threshold(depths) for depths in trees if len(depths) == leaves]
    observed = max(values, default=Fraction(0))
    assert observed == target, (leaves, observed, target)
    print(f"leaves={leaves}; depth_multisets={len(values)}; best_k={observed}")

# For m >= 8 leaves, the sum of all leaf upper bounds is 1 + (m - 1)k.
# If all three grouped parts are below 1/2, this sum must be below 3/2,
# forcing k < 1/(2(m-1)) <= 1/14 < 1/13.
assert Fraction(1, 14) < Fraction(1, 13)
print("leaves>=8: total-mass bound gives k<1/(2*(m-1))<=1/14")
print("optimal threshold within recursive binary-split-and-group scheme: k<1/13")
