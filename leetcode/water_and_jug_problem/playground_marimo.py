import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_measure_water, run_can_measure_water
    from solution import Solution

    return Solution, assert_can_measure_water, run_can_measure_water


@app.cell
def _():
    # Example test case
    x = 3
    y = 5
    target = 4
    expected = True
    return expected, target, x, y


@app.cell
def _(Solution, run_can_measure_water, target, x, y):
    result = run_can_measure_water(Solution, x, y, target)
    result
    return (result,)


@app.cell
def _(assert_can_measure_water, expected, result):
    assert_can_measure_water(result, expected)
    return


if __name__ == "__main__":
    app.run()
