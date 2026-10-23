import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_are_almost_equal, run_are_almost_equal
    from solution import Solution

    return Solution, assert_are_almost_equal, run_are_almost_equal


@app.cell
def _():
    # Example test case
    s1 = "bank"
    s2 = "kanb"
    expected = True
    return expected, s1, s2


@app.cell
def _(Solution, run_are_almost_equal, s1, s2):
    result = run_are_almost_equal(Solution, s1, s2)
    result
    return (result,)


@app.cell
def _(assert_are_almost_equal, expected, result):
    assert_are_almost_equal(result, expected)
    return


if __name__ == "__main__":
    app.run()
