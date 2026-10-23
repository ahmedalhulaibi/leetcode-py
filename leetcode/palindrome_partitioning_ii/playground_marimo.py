import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_cut, run_min_cut
    from solution import Solution

    return Solution, assert_min_cut, run_min_cut


@app.cell
def _():
    # Example test case
    s = "aab"
    expected = 1
    return expected, s


@app.cell
def _(Solution, run_min_cut, s):
    result = run_min_cut(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_min_cut, expected, result):
    assert_min_cut(result, expected)
    return


if __name__ == "__main__":
    app.run()
