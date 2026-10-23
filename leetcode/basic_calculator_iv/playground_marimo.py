import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_basic_calculator_iv, run_basic_calculator_iv
    from solution import Solution

    return Solution, assert_basic_calculator_iv, run_basic_calculator_iv


@app.cell
def _():
    # Example test case
    expression = "e + 8 - a + 5"
    evalvars = ["e"]
    evalints = [1]
    expected = ["-1*a", "14"]
    return evalints, evalvars, expected, expression


@app.cell
def _(Solution, evalints, evalvars, expression, run_basic_calculator_iv):
    result = run_basic_calculator_iv(Solution, expression, evalvars, evalints)
    result
    return (result,)


@app.cell
def _(assert_basic_calculator_iv, expected, result):
    assert_basic_calculator_iv(result, expected)
    return


if __name__ == "__main__":
    app.run()
