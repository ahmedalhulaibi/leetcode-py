import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_least_bricks, run_least_bricks
    from solution import Solution

    return Solution, assert_least_bricks, run_least_bricks


@app.cell
def _():
    # Example test case
    wall: list[list[int]] = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    expected = 2
    return expected, wall


@app.cell
def _(Solution, run_least_bricks, wall: list[list[int]]):
    result = run_least_bricks(Solution, wall)
    result
    return (result,)


@app.cell
def _(assert_least_bricks, expected, result):
    assert_least_bricks(result, expected)
    return


if __name__ == "__main__":
    app.run()
