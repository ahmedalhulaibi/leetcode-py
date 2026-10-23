import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_path_sum, run_min_path_sum
    from solution import Solution

    return Solution, assert_min_path_sum, run_min_path_sum


@app.cell
def _():
    # Example test case
    grid: list[list[int]] = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    expected = 7
    return expected, grid


@app.cell
def _(Solution, grid: list[list[int]], run_min_path_sum):
    result = run_min_path_sum(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_min_path_sum, expected, result):
    assert_min_path_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
