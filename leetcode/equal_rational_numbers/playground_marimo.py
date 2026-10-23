import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_rational_equal, run_is_rational_equal
    from solution import Solution

    return Solution, assert_is_rational_equal, run_is_rational_equal


@app.cell
def _():
    # Example test case
    s = "0.(52)"
    t = "0.5(25)"
    expected = True
    return expected, s, t


@app.cell
def _(Solution, run_is_rational_equal, s, t):
    result = run_is_rational_equal(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_is_rational_equal, expected, result):
    assert_is_rational_equal(result, expected)
    return


if __name__ == "__main__":
    app.run()
