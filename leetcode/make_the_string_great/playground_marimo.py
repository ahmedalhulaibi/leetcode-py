import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_make_good, run_make_good
    from solution import Solution

    return Solution, assert_make_good, run_make_good


@app.cell
def _():
    # Example test case
    s = "leEeetcode"
    expected = "leetcode"
    return expected, s


@app.cell
def _(Solution, run_make_good, s):
    result = run_make_good(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_make_good, expected, result):
    assert_make_good(result, expected)
    return


if __name__ == "__main__":
    app.run()
