import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_cost_climbing_stairs, run_min_cost_climbing_stairs
    from solution import Solution

    return (
        Solution,
        assert_min_cost_climbing_stairs,
        run_min_cost_climbing_stairs,
    )


@app.cell
def _():
    # Example test case
    cost = [10, 15, 20]
    expected = 15
    return cost, expected


@app.cell
def _(Solution, cost, run_min_cost_climbing_stairs):
    result = run_min_cost_climbing_stairs(Solution, cost)
    result
    return (result,)


@app.cell
def _(assert_min_cost_climbing_stairs, expected, result):
    assert_min_cost_climbing_stairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
