import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_obstacles, run_minimum_obstacles
    from solution import Solution

    return Solution, assert_minimum_obstacles, run_minimum_obstacles


@app.cell
def _():
    # Example test case
    grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
    expected = 2
    return expected, grid


@app.cell
def _(Solution, grid, run_minimum_obstacles):
    result = run_minimum_obstacles(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_minimum_obstacles, expected, result):
    assert_minimum_obstacles(result, expected)
    return


if __name__ == "__main__":
    app.run()
