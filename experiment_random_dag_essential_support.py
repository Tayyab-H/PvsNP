"""Finite canary for one random-DAG distribution of small Boolean circuits.

This is an exploratory sampler experiment, not an asymptotic lower-bound test.
It uses only the Python standard library and fixed seeds for reproducibility.
"""

from __future__ import annotations

import random


def random_circuit_truth_table(n: int, gate_count: int, rng: random.Random) -> int:
    """Return an N-bit table from a random AND/OR/NOT DAG with n inputs."""
    table_size = 1 << n
    mask = (1 << table_size) - 1
    wires: list[int] = []

    for variable in range(n):
        truth_table = 0
        for address in range(table_size):
            if (address >> variable) & 1:
                truth_table |= 1 << address
        wires.append(truth_table)

    wires.extend((0, mask))
    for _ in range(gate_count):
        operation = rng.randrange(3)
        available = len(wires)
        left = wires[rng.randrange(available)]

        if operation == 2:
            output = mask ^ left
        else:
            right = wires[rng.randrange(available)]
            output = left & right if operation == 0 else left | right
        wires.append(output)

    return wires[rng.randrange(len(wires))]


def essential_variable_count(truth_table: int, n: int) -> int:
    """Count address variables with at least one differing adjacent pair."""
    essential = 0
    for variable in range(n):
        step = 1 << variable
        depends_on_variable = any(
            ((truth_table >> address) & 1)
            != ((truth_table >> (address | step)) & 1)
            for address in range(1 << n)
            if not ((address >> variable) & 1)
        )
        essential += depends_on_variable
    return essential


def run_group(multiplier: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    for n in (6, 8, 10):
        gate_count = multiplier * n
        accepted = 0
        histogram = [0] * (n + 1)
        for _ in range(trials):
            table = random_circuit_truth_table(n, gate_count, rng)
            support = essential_variable_count(table, n)
            histogram[support] += 1
            accepted += support < n
        print(
            f"n={n} gates={gate_count} samples={trials} "
            f"accept={accepted / trials:.4f} support_hist={histogram}"
        )


if __name__ == "__main__":
    run_group(multiplier=150, trials=2_000, seed=48_702)
    run_group(multiplier=1_000, trials=300, seed=48_703)
