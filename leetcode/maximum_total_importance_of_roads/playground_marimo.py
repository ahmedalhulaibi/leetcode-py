import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_importance, run_maximum_importance
    from solution import Solution

    return Solution, assert_maximum_importance, run_maximum_importance


@app.cell
def _():
    # Example test case
    n = 5
    roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    expected = 43
    return expected, n, roads


@app.cell
def _(Solution, n, roads, run_maximum_importance):
    result = run_maximum_importance(Solution, n, roads)
    result
    return (result,)


@app.cell
def _(assert_maximum_importance, expected, result):
    assert_maximum_importance(result, expected)
    return


if __name__ == "__main__":
    app.run()
