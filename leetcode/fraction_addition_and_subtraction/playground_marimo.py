import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_fraction_addition, run_fraction_addition
    from solution import Solution

    return Solution, assert_fraction_addition, run_fraction_addition


@app.cell
def _():
    # Example test case
    expression = "-1/2+1/2"
    expected = "0/1"
    return expected, expression


@app.cell
def _(Solution, expression, run_fraction_addition):
    result = run_fraction_addition(Solution, expression)
    result
    return (result,)


@app.cell
def _(assert_fraction_addition, expected, result):
    assert_fraction_addition(result, expected)
    return


if __name__ == "__main__":
    app.run()
