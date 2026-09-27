"""Finite illustration: low-order public syntax can hide joint decodability.

Find a 12-by-12 invertible binary linear transform such that no set of up to
three public coordinates determines any individual message bit. The complete
public vector still determines the full message by Gaussian elimination.
"""

import random
from itertools import combinations, product


N = 12
MAX_OBSERVED_COORDINATES = 3
rng = random.Random(20260923)


def rank(rows):
    basis = {}
    for row in rows:
        value = row
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def contains_in_span(rows, target):
    span = {0}
    for row in rows:
        span |= {value ^ row for value in tuple(span)}
    return target in span


def encode(message, rows):
    return tuple((row & message).bit_count() & 1 for row in rows)


def decode(public, rows):
    """Solve A*x=public by Gaussian elimination over GF(2)."""
    if isinstance(public, int):
        public = tuple((public >> i) & 1 for i in range(N))
    matrix = [rows[i] | (public[i] << N) for i in range(N)]
    pivot_row = 0
    for column in range(N):
        selected = next((r for r in range(pivot_row, N) if (matrix[r] >> column) & 1), None)
        assert selected is not None
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        for r in range(N):
            if r != pivot_row and ((matrix[r] >> column) & 1):
                matrix[r] ^= matrix[pivot_row]
        pivot_row += 1
    return tuple((matrix[i] >> N) & 1 for i in range(N))


for trial in range(1, 100_001):
    rows = tuple(rng.getrandbits(N) for _ in range(N))
    if rank(rows) != N:
        continue
    good = True
    for size in range(1, MAX_OBSERVED_COORDINATES + 1):
        for chosen in combinations(rows, size):
            if any(contains_in_span(chosen, 1 << j) for j in range(N)):
                good = False
                break
        if not good:
            break
    if good:
        break
else:
    raise AssertionError("no suitable transform found in the search budget")

messages = range(1 << N)
encoded = {message: encode(message, rows) for message in messages}
assert len(set(encoded.values())) == 1 << N
assert all(
    sum((bit << j) for j, bit in enumerate(decode(public, rows))) == message
    for message, public in encoded.items()
)

# For uniform message bits, observing a set of linear forms reveals target bit
# j iff the unit vector e_j lies in the row span. The search checked every
# public subset of size at most three, exactly.
for size in range(1, MAX_OBSERVED_COORDINATES + 1):
    for indices in combinations(range(N), size):
        selected = tuple(rows[i] for i in indices)
        assert all(not contains_in_span(selected, 1 << j) for j in range(N))

# Despite that low-order independence, each target has an opposite-phase
# coupling whose paired public strings differ in exactly one coordinate.
# The coordinate used can depend on the target bit; each fixed public-bit
# marginal is still identical in both phases.
one_bit_flip_couplings = []
for target_coordinate in range(N):
    decoder_support = [
        public_coordinate
        for public_coordinate in range(N)
        if decode(1 << public_coordinate, rows)[target_coordinate] == 1
    ]
    assert len(decoder_support) > MAX_OBSERVED_COORDINATES
    chosen_coordinate = decoder_support[0]
    public_delta = 1 << chosen_coordinate
    witness_delta = sum(
        bit << j for j, bit in enumerate(decode(public_delta, rows))
    )
    assert (witness_delta >> target_coordinate) & 1
    for message in messages:
        if ((message >> target_coordinate) & 1) == 0:
            public0 = encoded[message]
            public1 = tuple(
                bit ^ (1 if i == chosen_coordinate else 0)
                for i, bit in enumerate(public0)
            )
            message1 = sum(
                bit << j for j, bit in enumerate(decode(public1, rows))
            )
            assert ((message1 >> target_coordinate) & 1) == 1
            assert sum(a != b for a, b in zip(public0, public1)) == 1
    one_bit_flip_couplings.append((target_coordinate, chosen_coordinate, len(decoder_support)))

print(f"message bits: {N}; public bits: {N}; candidates examined: {trial}")
print("matrix rows (hex, low bit is input coordinate 0):", tuple(f"{row:03x}" for row in rows))
print(f"no subset of at most {MAX_OBSERVED_COORDINATES} public bits determines any one message bit")
print("the full public vector is invertible and a fixed Gaussian-elimination decoder recovers all message bits")
print("inverse-row weights:", tuple(weight for _, _, weight in one_bit_flip_couplings))
print("yet each target admits an opposite-phase coupling differing in exactly one public coordinate")
print("scope: finite syntax-vs-semantics example, not an asymptotic lower bound or P-vs-NP result")
