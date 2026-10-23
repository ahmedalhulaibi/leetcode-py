import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_groups, run_min_groups
    from solution import Solution

    return Solution, assert_min_groups, run_min_groups


@app.cell
def _():
    # Example test case
    intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
    expected = 3
    return expected, intervals


@app.cell
def _(Solution, intervals, run_min_groups):
    result = run_min_groups(Solution, intervals)
    result
    return (result,)


@app.cell
def _(assert_min_groups, expected, result):
    assert_min_groups(result, expected)
    return


if __name__ == "__main__":
    app.run()
