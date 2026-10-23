import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_cost_ii, run_min_cost_ii
    from solution import Solution

    return Solution, assert_min_cost_ii, run_min_cost_ii


@app.cell
def _():
    # Example test case
    costs = [[1, 5, 3], [2, 9, 4]]
    expected = 5
    return costs, expected


@app.cell
def _(Solution, costs, run_min_cost_ii):
    result = run_min_cost_ii(Solution, costs)
    result
    return (result,)


@app.cell
def _(assert_min_cost_ii, expected, result):
    assert_min_cost_ii(result, expected)
    return


if __name__ == "__main__":
    app.run()
