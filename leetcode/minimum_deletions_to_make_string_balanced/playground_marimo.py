import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_deletions, run_minimum_deletions
    from solution import Solution

    return Solution, assert_minimum_deletions, run_minimum_deletions


@app.cell
def _():
    # Example test case
    s = "aababbab"
    expected = 2
    return expected, s


@app.cell
def _(Solution, run_minimum_deletions, s):
    result = run_minimum_deletions(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_minimum_deletions, expected, result):
    assert_minimum_deletions(result, expected)
    return


if __name__ == "__main__":
    app.run()
