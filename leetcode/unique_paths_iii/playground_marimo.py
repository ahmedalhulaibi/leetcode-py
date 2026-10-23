import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_unique_paths_iii, run_unique_paths_iii
    from solution import Solution

    return Solution, assert_unique_paths_iii, run_unique_paths_iii


@app.cell
def _():
    # Example test case
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    expected = 2
    return expected, grid


@app.cell
def _(Solution, grid, run_unique_paths_iii):
    result = run_unique_paths_iii(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_unique_paths_iii, expected, result):
    assert_unique_paths_iii(result, expected)
    return


if __name__ == "__main__":
    app.run()
