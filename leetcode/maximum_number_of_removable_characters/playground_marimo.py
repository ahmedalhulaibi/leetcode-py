import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_removals, run_maximum_removals
    from solution import Solution

    return Solution, assert_maximum_removals, run_maximum_removals


@app.cell
def _():
    # Example test case
    s = "abcacb"
    p = "ab"
    removable = [3, 1, 0]
    expected = 2
    return expected, p, removable, s


@app.cell
def _(Solution, p, removable, run_maximum_removals, s):
    result = run_maximum_removals(Solution, s, p, removable)
    result
    return (result,)


@app.cell
def _(assert_maximum_removals, expected, result):
    assert_maximum_removals(result, expected)
    return


if __name__ == "__main__":
    app.run()
