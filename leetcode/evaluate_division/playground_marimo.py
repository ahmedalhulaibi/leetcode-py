import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_calc_equation, run_calc_equation
    from solution import Solution

    return Solution, assert_calc_equation, run_calc_equation


@app.cell
def _():
    # Example test case
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]
    return equations, expected, queries, values


@app.cell
def _(Solution, equations, queries, run_calc_equation, values):
    result = run_calc_equation(Solution, equations, values, queries)
    result
    return (result,)


@app.cell
def _(assert_calc_equation, expected, result):
    assert_calc_equation(result, expected)
    return


if __name__ == "__main__":
    app.run()
