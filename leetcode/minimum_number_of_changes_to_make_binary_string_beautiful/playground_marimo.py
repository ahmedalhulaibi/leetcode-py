import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_changes, run_min_changes
    from solution import Solution

    return Solution, assert_min_changes, run_min_changes


@app.cell
def _():
    # Example test case
    s = "1001"
    expected = 2
    return expected, s


@app.cell
def _(Solution, run_min_changes, s):
    result = run_min_changes(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_min_changes, expected, result):
    assert_min_changes(result, expected)
    return


if __name__ == "__main__":
    app.run()
