import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_car_fleet, run_car_fleet
    from solution import Solution

    return Solution, assert_car_fleet, run_car_fleet


@app.cell
def _():
    # Example test case
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    expected = 3
    return expected, position, speed, target


@app.cell
def _(Solution, position, run_car_fleet, speed, target):
    result = run_car_fleet(Solution, target, position, speed)
    result
    return (result,)


@app.cell
def _(assert_car_fleet, expected, result):
    assert_car_fleet(result, expected)
    return


if __name__ == "__main__":
    app.run()
