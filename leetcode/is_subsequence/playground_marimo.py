import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_subsequence, run_is_subsequence
    from solution import Solution

    return Solution, assert_is_subsequence, run_is_subsequence


@app.cell
def _():
    # Example test case
    s = "abc"
    t = "ahbgdc"
    expected = True
    return expected, s, t


@app.cell
def _(Solution, run_is_subsequence, s, t):
    result = run_is_subsequence(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_is_subsequence, expected, result):
    assert_is_subsequence(result, expected)
    return


if __name__ == "__main__":
    app.run()
