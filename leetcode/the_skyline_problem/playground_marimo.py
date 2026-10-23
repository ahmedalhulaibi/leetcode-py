import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_skyline, run_get_skyline
    from solution import Solution

    return Solution, assert_get_skyline, run_get_skyline


@app.cell
def _():
    # Example test case
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    expected = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    return buildings, expected


@app.cell
def _(Solution, buildings, run_get_skyline):
    result = run_get_skyline(Solution, buildings)
    result
    return (result,)


@app.cell
def _(assert_get_skyline, expected, result):
    assert_get_skyline(result, expected)
    return


if __name__ == "__main__":
    app.run()
