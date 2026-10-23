import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_unique_paths_with_obstacles, run_unique_paths_with_obstacles
    from solution import Solution

    return (
        Solution,
        assert_unique_paths_with_obstacles,
        run_unique_paths_with_obstacles,
    )


@app.cell
def _():
    # Example test case
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected = 2
    return expected, grid


@app.cell
def _(Solution, grid, run_unique_paths_with_obstacles):
    result = run_unique_paths_with_obstacles(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_unique_paths_with_obstacles, expected, result):
    assert_unique_paths_with_obstacles(result, expected)
    return


if __name__ == "__main__":
    app.run()
