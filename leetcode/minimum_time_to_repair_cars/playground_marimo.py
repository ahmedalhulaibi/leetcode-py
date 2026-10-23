import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_repair_cars, run_repair_cars
    from solution import Solution

    return Solution, assert_repair_cars, run_repair_cars


@app.cell
def _():
    # Example test case
    ranks = [4, 2, 3, 1]
    cars = 10
    expected = 16
    return cars, expected, ranks


@app.cell
def _(Solution, cars, ranks, run_repair_cars):
    result = run_repair_cars(Solution, ranks, cars)
    result
    return (result,)


@app.cell
def _(assert_repair_cars, expected, result):
    assert_repair_cars(result, expected)
    return


if __name__ == "__main__":
    app.run()
