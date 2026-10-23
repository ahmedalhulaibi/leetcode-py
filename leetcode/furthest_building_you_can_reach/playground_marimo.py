import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_furthest_building, run_furthest_building
    from solution import Solution

    return Solution, assert_furthest_building, run_furthest_building


@app.cell
def _():
    # Example test case
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    expected = 4
    return bricks, expected, heights, ladders


@app.cell
def _(Solution, bricks, heights, ladders, run_furthest_building):
    result = run_furthest_building(Solution, heights, bricks, ladders)
    result
    return (result,)


@app.cell
def _(assert_furthest_building, expected, result):
    assert_furthest_building(result, expected)
    return


if __name__ == "__main__":
    app.run()
