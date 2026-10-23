import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import (
        assert_longest_substring_with_at_least_k_repeating_characters,
        run_longest_substring_with_at_least_k_repeating_characters,
    )
    from solution import Solution

    return (
        Solution,
        assert_longest_substring_with_at_least_k_repeating_characters,
        run_longest_substring_with_at_least_k_repeating_characters,
    )


@app.cell
def _():
    # Example test case
    s = "aaabb"
    k = 3
    expected = 3
    return expected, k, s


@app.cell
def _(
    Solution,
    k,
    run_longest_substring_with_at_least_k_repeating_characters,
    s,
):
    result = run_longest_substring_with_at_least_k_repeating_characters(Solution, s, k)
    result
    return (result,)


@app.cell
def _(
    assert_longest_substring_with_at_least_k_repeating_characters,
    expected,
    result,
):
    assert_longest_substring_with_at_least_k_repeating_characters(result, expected)
    return


if __name__ == "__main__":
    app.run()
