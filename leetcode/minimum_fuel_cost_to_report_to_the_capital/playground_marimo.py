import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_fuel_cost, run_minimum_fuel_cost
    from solution import Solution

    return Solution, assert_minimum_fuel_cost, run_minimum_fuel_cost


@app.cell
def _():
    # Example test case
    roads = [[0, 1], [0, 2], [0, 3]]
    seats = 5
    expected = 3
    return expected, roads, seats


@app.cell
def _(Solution, roads, run_minimum_fuel_cost, seats):
    result = run_minimum_fuel_cost(Solution, roads, seats)
    result
    return (result,)


@app.cell
def _(assert_minimum_fuel_cost, expected, result):
    assert_minimum_fuel_cost(result, expected)
    return


if __name__ == "__main__":
    app.run()
