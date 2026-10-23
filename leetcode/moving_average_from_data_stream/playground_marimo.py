import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_moving_average, run_moving_average
    from solution import MovingAverage

    return MovingAverage, assert_moving_average, run_moving_average


@app.cell
def _():
    # Example test case
    operations = ["MovingAverage", "next", "next", "next", "next"]
    inputs = [[3], [1], [10], [3], [5]]
    expected = [None, 1.0, 5.5, 14 / 3, 6.0]
    return expected, inputs, operations


@app.cell
def _(MovingAverage, inputs, operations, run_moving_average):
    result, average = run_moving_average(MovingAverage, operations, inputs)
    print(result)
    average
    return (result,)


@app.cell
def _(assert_moving_average, expected, result):
    assert_moving_average(result, expected)
    return


if __name__ == "__main__":
    app.run()
