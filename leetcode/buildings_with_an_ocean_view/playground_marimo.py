import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_buildings, run_find_buildings
    from solution import Solution

    return Solution, assert_find_buildings, run_find_buildings


@app.cell
def _():
    # Example test case
    heights = [4, 2, 3, 1]
    expected = [0, 2, 3]
    return expected, heights


@app.cell
def _(Solution, heights, run_find_buildings):
    result = run_find_buildings(Solution, heights)
    result
    return (result,)


@app.cell
def _(assert_find_buildings, expected, result):
    assert_find_buildings(result, expected)
    return


if __name__ == "__main__":
    app.run()
