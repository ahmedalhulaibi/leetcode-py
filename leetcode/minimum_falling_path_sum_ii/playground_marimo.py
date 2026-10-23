import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_falling_path_sum, run_min_falling_path_sum
    from solution import Solution

    return Solution, assert_min_falling_path_sum, run_min_falling_path_sum


@app.cell
def _():
    # Example test case
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = 13
    return expected, grid


@app.cell
def _(Solution, grid, run_min_falling_path_sum):
    result = run_min_falling_path_sum(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_min_falling_path_sum, expected, result):
    assert_min_falling_path_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
