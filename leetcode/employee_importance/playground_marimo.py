import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_importance, run_get_importance
    from solution import Solution

    return Solution, assert_get_importance, run_get_importance


@app.cell
def _():
    # Example test case
    employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    id = 1
    expected = 11
    return employees, expected, id


@app.cell
def _(Solution, employees, id, run_get_importance):
    result = run_get_importance(Solution, employees, id)
    result
    return (result,)


@app.cell
def _(assert_get_importance, expected, result):
    assert_get_importance(result, expected)
    return


if __name__ == "__main__":
    app.run()
