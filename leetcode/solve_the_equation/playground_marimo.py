import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_solve_equation, run_solve_equation
    from solution import Solution

    return Solution, assert_solve_equation, run_solve_equation


@app.cell
def _():
    # Example test case
    equation = "x+5-3+x=6+x-2"
    expected = "x=2"
    return equation, expected


@app.cell
def _(Solution, equation, run_solve_equation):
    result = run_solve_equation(Solution, equation)
    result
    return (result,)


@app.cell
def _(assert_solve_equation, expected, result):
    assert_solve_equation(result, expected)
    return


if __name__ == "__main__":
    app.run()
