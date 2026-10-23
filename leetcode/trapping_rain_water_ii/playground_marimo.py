import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_trap_rain_water, run_trap_rain_water
    from solution import Solution

    return Solution, assert_trap_rain_water, run_trap_rain_water


@app.cell
def _():
    # Example test case
    height_map = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    expected = 4
    return expected, height_map


@app.cell
def _(Solution, height_map, run_trap_rain_water):
    result = run_trap_rain_water(Solution, height_map)
    result
    return (result,)


@app.cell
def _(assert_trap_rain_water, expected, result):
    assert_trap_rain_water(result, expected)
    return


if __name__ == "__main__":
    app.run()
