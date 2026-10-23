import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_evaluate, run_evaluate
    from solution import Solution

    return Solution, assert_evaluate, run_evaluate


@app.cell
def _():
    # Example test case
    expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
    expected = 14
    return expected, expression


@app.cell
def _(Solution, expression, run_evaluate):
    result = run_evaluate(Solution, expression)
    result
    return (result,)


@app.cell
def _(assert_evaluate, expected, result):
    assert_evaluate(result, expected)
    return


if __name__ == "__main__":
    app.run()
