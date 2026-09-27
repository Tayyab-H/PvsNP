"""Finite sanity check for Proposition 18.12.

On the 6-bit cube, remove one point and use codimension-two certificates.
The proposition proves the four-pair cover for the stated density condition;
this script checks every anchor and certificate on this small instance.
"""

from itertools import combinations


N = 6
R = 2
U = set(range(1 << N)) - {0}
I = (0, 1)
J = (2, 3)


def bit(word, coordinate):
    return (word >> coordinate) & 1


def parity(word, coordinates):
    return sum(bit(word, i) for i in coordinates) % 2


def cylinder(anchor, coordinates):
    return {
        word for word in U
        if all(bit(word, i) == bit(anchor, i) for i in coordinates)
    }


def in_filter(anchor, subset):
    return any(cylinder(anchor, coordinates) <= subset
               for coordinates in combinations(range(N), R))


def main():
    assert len(set(range(1 << N)) - U) < 2 ** (N - R - 1)
    checked = 0
    for anchor in range(1 << N):
        p = parity(anchor, I)
        q = parity(anchor, J)
        e = {word for word in U if parity(word, I) == p}
        h = {word for word in U if parity(word, J) == q}
        intersection = e & h
        assert in_filter(anchor, e)
        assert in_filter(anchor, h)
        assert not in_filter(anchor, intersection)
        checked += 1
    print(f"PASS: four parity choices cover all {checked} anchors "
          f"for N={N}, r={R}, |U^c|={2**N-len(U)}")


if __name__ == "__main__":
    main()
