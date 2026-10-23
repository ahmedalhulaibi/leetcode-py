import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_cost_to_supply_water, run_min_cost_to_supply_water
    from solution import Solution

    return (
        Solution,
        assert_min_cost_to_supply_water,
        run_min_cost_to_supply_water,
    )


@app.cell
def _():
    # Example test case
    n = 3
    wells = [1, 2, 2]
    pipes = [[1, 2, 1], [2, 3, 1]]
    expected = 3
    return expected, n, pipes, wells


@app.cell
def _(Solution, n, pipes, run_min_cost_to_supply_water, wells):
    result = run_min_cost_to_supply_water(Solution, n, wells, pipes)
    result
    return (result,)


@app.cell
def _(assert_min_cost_to_supply_water, expected, result):
    assert_min_cost_to_supply_water(result, expected)
    return


if __name__ == "__main__":
    app.run()
