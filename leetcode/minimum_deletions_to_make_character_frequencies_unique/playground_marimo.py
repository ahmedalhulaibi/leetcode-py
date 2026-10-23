import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_deletions, run_min_deletions
    from solution import Solution

    return Solution, assert_min_deletions, run_min_deletions


@app.cell
def _():
    # Example test case
    s = "aaabbbcc"
    expected = 2
    return expected, s


@app.cell
def _(Solution, run_min_deletions, s):
    result = run_min_deletions(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_min_deletions, expected, result):
    assert_min_deletions(result, expected)
    return


if __name__ == "__main__":
    app.run()
