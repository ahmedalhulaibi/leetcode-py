import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_special_equivalent_groups, run_num_special_equivalent_groups
    from solution import Solution

    return (
        Solution,
        assert_num_special_equivalent_groups,
        run_num_special_equivalent_groups,
    )


@app.cell
def _():
    # Example test case
    words = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
    expected = 3
    return expected, words


@app.cell
def _(Solution, run_num_special_equivalent_groups, words):
    result = run_num_special_equivalent_groups(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_num_special_equivalent_groups, expected, result):
    assert_num_special_equivalent_groups(result, expected)
    return


if __name__ == "__main__":
    app.run()
