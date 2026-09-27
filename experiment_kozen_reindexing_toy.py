"""Finite sanity check for a tailored diagonal indexing.

Base class: eventually constant Boolean sequences.  Target diagonal:
g(e) = e mod 2, which is computable but is not in that class.

The finite run checks only a prefix; the infinite correctness argument is in
ideas.md, Idea 14.
"""

from itertools import count


def descriptions():
    """Enumerate (prefix_length, little_endian_prefix, eventual_tail)."""
    for length in count():
        for prefix in range(1 << length):
            for tail in (0, 1):
                yield length, prefix, tail


def value(description, n):
    length, prefix, tail = description
    if n < length:
        return (prefix >> n) & 1
    return tail


def target(n):
    return n & 1


def main():
    how_many = 32
    base = []
    source = descriptions()
    previous = -1
    reserved = {}

    for j in range(how_many):
        description = next(source)
        base.append(description)
        for e in count(previous + 1):
            if value(description, e) != target(e):
                reserved[e] = j
                previous = e
                break

    max_index = previous

    def indexed_value(e, x):
        if e in reserved:
            return value(base[reserved[e]], x)
        return 1 - target(e)

    assert len(reserved) == how_many
    assert len(set(reserved)) == how_many
    for e in range(max_index + 1):
        assert indexed_value(e, e) == 1 - target(e)
        assert 1 - indexed_value(e, e) == target(e)

    print(f"base functions assigned: {how_many}")
    print(f"distinct reserved indices: {len(reserved)}")
    print(f"diagonal identity checked for every index 0..{max_index}")
    print("target g(e)=e mod 2 is not eventually constant")
    print("scope: finite implementation check; no complexity separation")


if __name__ == "__main__":
    main()
