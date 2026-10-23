import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_calculate, run_calculate
    from solution import Solution

    return Solution, assert_calculate, run_calculate


@app.cell
def _():
    # Example test case
    s = "3+2*2"
    expected = 7
    return expected, s


@app.cell
def _(Solution, run_calculate, s):
    result = run_calculate(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_calculate, expected, result):
    assert_calculate(result, expected)
    return


if __name__ == "__main__":
    app.run()
