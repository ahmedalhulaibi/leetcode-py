import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_equations_possible, run_equations_possible
    from solution import Solution

    return Solution, assert_equations_possible, run_equations_possible


@app.cell
def _():
    # Example test case
    equations = ["a==b", "b!=a"]
    expected = False
    return equations, expected


@app.cell
def _(Solution, equations, run_equations_possible):
    result = run_equations_possible(Solution, equations)
    result
    return (result,)


@app.cell
def _(assert_equations_possible, expected, result):
    assert_equations_possible(result, expected)
    return


if __name__ == "__main__":
    app.run()
