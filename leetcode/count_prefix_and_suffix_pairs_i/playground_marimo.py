import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_prefix_suffix_pairs, run_count_prefix_suffix_pairs
    from solution import Solution

    return (
        Solution,
        assert_count_prefix_suffix_pairs,
        run_count_prefix_suffix_pairs,
    )


@app.cell
def _():
    # Example test case
    words = ["a", "aba", "ababa", "aa"]
    expected = 4
    return expected, words


@app.cell
def _(Solution, run_count_prefix_suffix_pairs, words):
    result = run_count_prefix_suffix_pairs(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_count_prefix_suffix_pairs, expected, result):
    assert_count_prefix_suffix_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
