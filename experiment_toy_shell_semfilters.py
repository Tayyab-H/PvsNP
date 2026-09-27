"""Five-point constant-weight shell instance for the all-semi-filter search."""

import experiment_toy_all_semfilters_5point as search


search.N_BITS = 5
search.U_WORDS = [word for word in range(1 << search.N_BITS)
                  if word.bit_count() == 4]
search.ANCHORS = [anchor for anchor in range(1 << search.N_BITS)
                  if anchor.bit_count() <= 1]
search.M = len(search.U_WORDS)
search.SET_COUNT = 1 << search.M
search.FULL_U = search.SET_COUNT - 1

search.main()


def verify_general_shell(n, radius):
    assert n >= 2 * radius + 2
    point_count = n
    indices = list(range(point_count))
    cut = radius + 1
    left = set(indices[:cut])
    right = set(indices[cut:])
    assert len(left) >= radius + 1 and len(right) >= radius + 1
    left_mask = sum(1 << i for i in left)
    right_mask = sum(1 << i for i in right)
    full_mask = (1 << point_count) - 1
    for anchor in range(1 << n):
        if anchor.bit_count() > radius:
            continue
        generators = []
        for coordinate in range(n):
            if ((anchor >> coordinate) & 1) == 0:
                generators.append(1 << coordinate)
            else:
                generators.append(full_mask ^ (1 << coordinate))
        assert any((left_mask & gen) == gen for gen in generators)
        assert any((right_mask & gen) == gen for gen in generators)
    return 1


checks = 0
for n in range(4, 11):
    for radius in range((n - 2) // 2 + 1):
        checks += verify_general_shell(n, radius)
print(f"co-singleton shell lemma checked for {checks} parameter pairs with n=4..10")
