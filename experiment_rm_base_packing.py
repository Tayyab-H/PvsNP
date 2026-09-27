"""Finite checks for a Reed--Muller generalized-weight/base-packing route.

Wei's generalized Hamming weight formula writes each subcode dimension q as
an admissible sum of binomial-prefix terms.  This script computes that
representation greedily and checks whether every resulting weight d_q obeys
d_q - 2q >= 2^(N-d) - 2 for small parameters.

The experiment is diagnostic only; the asymptotic theorem still needs a
written proof of the displayed inequality from the admissible expansion.
"""

from math import comb


def prefix(m: int, r: int) -> int:
    return sum(comb(m, j) for j in range(r + 1))


def wei_weight_hierarchy(n: int, degree: int) -> list[int]:
    """Return d_q(RM(n, degree)), q=1..sum_{j<=degree} C(n,j).

    Wei's representation has terms C(m_i, <= r_i) with
    m_i-r_i=n-degree-i+1, and strictly decreasing m_i.  At each index the
    greedy largest admissible term is unique.
    """
    dimension = sum(comb(n, j) for j in range(degree + 1))
    weights = []
    for q in range(1, dimension + 1):
        remaining = q
        previous_m = n + 1
        i = 1
        support = 0
        while remaining:
            gap = n - degree - i + 1
            best = None
            for m in range(min(n, previous_m - 1), gap - 1, -1):
                r = m - gap
                term = prefix(m, r)
                if term <= remaining:
                    best = (m, r, term)
                    break
            if best is None:
                raise ValueError((n, degree, q, i, remaining, previous_m))
            m, r, term = best
            remaining -= term
            support += 1 << m
            previous_m = m
            i += 1
            if i > n + 2:
                raise ValueError("representation failed to terminate")
        weights.append(support)
    return weights


def main() -> None:
    all_ok = True
    summaries = []
    for n in range(2, 17):
        for degree in range(0, (n - 1) // 2 + 1):
            dimension = sum(comb(n, j) for j in range(degree + 1))
            weights = wei_weight_hierarchy(n, degree)
            minimum_gap = min(w - 2 * q for q, w in enumerate(weights, start=1))
            bound = (1 << (n - degree)) - 2
            ok = minimum_gap >= bound
            all_ok &= ok
            if not ok:
                witness = min(
                    ((w - 2 * q, q, w) for q, w in enumerate(weights, start=1))
                )
                summaries.append((n, degree, dimension, bound, witness))
    print(f"all tested inequalities hold: {all_ok}")
    print("counterexamples:", summaries[:10])
    for n, degree in [(8, 3), (12, 5), (16, 7)]:
        if degree < n / 2:
            weights = wei_weight_hierarchy(n, degree)
            dimension = len(weights)
            minimum_gap = min(w - 2 * q for q, w in enumerate(weights, start=1))
            print(
                f"N={n}, d={degree}, D={dimension}, "
                f"delta={1 << (n-degree)}, min_q(d_q-2q)={minimum_gap}"
            )


if __name__ == "__main__":
    main()
