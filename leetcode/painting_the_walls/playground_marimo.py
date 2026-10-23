import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_paint_walls, run_paint_walls
    from solution import Solution

    return Solution, assert_paint_walls, run_paint_walls


@app.cell
def _():
    # Example test case
    cost = [1, 2, 3, 2]
    time = [1, 2, 3, 2]
    expected = 3
    return cost, expected, time


@app.cell
def _(Solution, cost, run_paint_walls, time):
    result = run_paint_walls(Solution, cost, time)
    result
    return (result,)


@app.cell
def _(assert_paint_walls, expected, result):
    assert_paint_walls(result, expected)
    return


if __name__ == "__main__":
    app.run()
