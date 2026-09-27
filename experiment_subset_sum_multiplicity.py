"""Demonstrate the set-versus-list convention in subset-sum counting.

This is not a counterexample to papers that define each instance as a set.
It only shows that repeated values are independently selectable in list form.
"""


def all_subset_sums(items: list[int]) -> set[int]:
    sums = {0}
    for value in items:
        sums |= {subtotal + value for subtotal in tuple(sums)}
    return sums


def main() -> None:
    r = 4
    multiplicity = 7
    base = multiplicity + 1
    values = [base**j for j in range(r)]
    items = [value for value in values for _ in range(multiplicity)]
    sums = all_subset_sums(items)

    expected = base**r
    assert len(set(values)) == r
    assert len(sums) == expected
    assert expected > 2**r
    print(
        f"{r} distinct values, multiplicity {multiplicity}, "
        f"{len(items)} items: {len(sums)} subset sums > 2^{r}={2**r}"
    )
    print("PASS: list instances count repeated choices; set instances collapse them")


if __name__ == "__main__":
    main()
