"""Finite check of Propositions 18.10 and 18.11's block covers.

The proposition has a direct proof for every block count and threshold. This
script checks the set-mask encoding and exhausts all anchor strings through
eight blocks; it is only an implementation sanity check.
"""

from itertools import product


# A mask uses bit i for element i+1 of the four-point local universe.
MINIMAL_WINNERS = (
    (0b0011, 0b1100, 0b0101, 0b1010),  # F_0: 12, 34, 13, 24
    (0b0011, 0b1100, 0b1001, 0b0110),  # F_1: 12, 34, 14, 23
    (0b0101, 0b1010, 0b1001, 0b0110),  # F_2: 13, 24, 14, 23
)


def local_member(subset, label):
    return any((subset & winner) == winner
               for winner in MINIMAL_WINNERS[label])


def global_member(blocks, anchor, threshold):
    return sum(local_member(block, label)
               for block, label in zip(blocks, anchor)) >= threshold


def pair_covers(pair, anchor, threshold):
    left, right = pair
    return (
        global_member(left, anchor, threshold)
        and global_member(right, anchor, threshold)
        and not global_member(
            tuple(x & y for x, y in zip(left, right)),
            anchor,
            threshold,
        )
    )


def global_member_under_g(blocks, anchor, g_table):
    status = sum(
        int(local_member(block, label)) << j
        for j, (block, label) in enumerate(zip(blocks, anchor))
    )
    return bool((g_table >> status) & 1)


def pair_covers_under_g(pair, anchor, g_table):
    left, right = pair
    intersection = tuple(x & y for x, y in zip(left, right))
    return (
        global_member_under_g(left, anchor, g_table)
        and global_member_under_g(right, anchor, g_table)
        and not global_member_under_g(intersection, anchor, g_table)
    )


def monotone_tables(k):
    input_count = 1 << k
    for table in range(1 << input_count):
        if (table & 1) or not ((table >> (input_count - 1)) & 1):
            continue
        monotone = True
        for x in range(input_count):
            if not ((table >> x) & 1):
                continue
            for y in range(input_count):
                if (x & y) == x and not ((table >> y) & 1):
                    monotone = False
                    break
            if not monotone:
                break
        if monotone:
            yield table


def main():
    pair_a = (
        lambda k: (0b0011,) * k,
        lambda k: (0b1100,) * k,
    )
    pair_b = (
        lambda k: (0b0111,) * k,
        lambda k: (0b1011,) * k,
    )

    threshold_checked = 0
    for k in range(1, 9):
        anchors = list(product(range(3), repeat=k))
        for threshold in range(1, k + 1):
            a_pair = (pair_a[0](k), pair_a[1](k))
            b_pair = (pair_b[0](k), pair_b[1](k))
            for anchor in anchors:
                x = sum(label in (0, 1) for label in anchor)
                a_hit = pair_covers(a_pair, anchor, threshold)
                b_hit = pair_covers(b_pair, anchor, threshold)
                assert a_hit == (x >= threshold)
                assert b_hit == (x < threshold)
                assert a_hit or b_hit
                threshold_checked += 1

    print(f"PASS: threshold identities checked on {threshold_checked:,} "
          "anchor-threshold instances for k=1..8")

    aggregator_checked = 0
    for k in range(1, 5):
        anchors = list(product(range(3), repeat=k))
        a_pair = (pair_a[0](k), pair_a[1](k))
        b_pair = (pair_b[0](k), pair_b[1](k))
        for g_table in monotone_tables(k):
            for anchor in anchors:
                a_hit = pair_covers_under_g(a_pair, anchor, g_table)
                b_hit = pair_covers_under_g(b_pair, anchor, g_table)
                x = sum(int(label in (0, 1)) << j
                        for j, label in enumerate(anchor))
                gx = bool((g_table >> x) & 1)
                assert a_hit == gx
                assert b_hit == (not gx)
                assert a_hit or b_hit
                aggregator_checked += 1

    print(f"PASS: arbitrary monotone-aggregator identities checked on "
          f"{aggregator_checked:,} instances for k=1..4")


if __name__ == "__main__":
    main()
