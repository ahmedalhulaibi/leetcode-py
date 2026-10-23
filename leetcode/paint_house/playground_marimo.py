import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_cost, run_min_cost
    from solution import Solution

    return Solution, assert_min_cost, run_min_cost


@app.cell
def _():
    # Example test case
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    expected = 10
    return costs, expected


@app.cell
def _(Solution, costs, run_min_cost):
    result = run_min_cost(Solution, costs)
    result
    return (result,)


@app.cell
def _(assert_min_cost, expected, result):
    assert_min_cost(result, expected)
    return


if __name__ == "__main__":
    app.run()
