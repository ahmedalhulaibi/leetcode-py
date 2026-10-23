import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_car_pooling, run_car_pooling
    from solution import Solution

    return Solution, assert_car_pooling, run_car_pooling


@app.cell
def _():
    # Example test case
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    expected = False
    return capacity, expected, trips


@app.cell
def _(Solution, capacity, run_car_pooling, trips):
    result = run_car_pooling(Solution, trips, capacity)
    result
    return (result,)


@app.cell
def _(assert_car_pooling, expected, result):
    assert_car_pooling(result, expected)
    return


if __name__ == "__main__":
    app.run()
