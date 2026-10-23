import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_refuel_stops, run_min_refuel_stops
    from solution import Solution

    return Solution, assert_min_refuel_stops, run_min_refuel_stops


@app.cell
def _():
    # Example test case
    target = 100
    start_fuel = 10
    stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
    expected = 2
    return expected, start_fuel, stations, target


@app.cell
def _(Solution, run_min_refuel_stops, start_fuel, stations, target):
    result = run_min_refuel_stops(Solution, target, start_fuel, stations)
    result
    return (result,)


@app.cell
def _(assert_min_refuel_stops, expected, result):
    assert_min_refuel_stops(result, expected)
    return


if __name__ == "__main__":
    app.run()
