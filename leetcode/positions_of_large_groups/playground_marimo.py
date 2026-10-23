import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_large_group_positions, run_large_group_positions
    from solution import Solution

    return Solution, assert_large_group_positions, run_large_group_positions


@app.cell
def _():
    # Example test case
    s = "abbxxxxzzy"
    expected = [[3, 6]]
    return expected, s


@app.cell
def _(Solution, run_large_group_positions, s):
    result = run_large_group_positions(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_large_group_positions, expected, result):
    assert_large_group_positions(result, expected)
    return


if __name__ == "__main__":
    app.run()
