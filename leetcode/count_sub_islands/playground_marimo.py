import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_sub_islands, run_count_sub_islands
    from solution import Solution

    return Solution, assert_count_sub_islands, run_count_sub_islands


@app.cell
def _():
    # Example test case
    grid1 = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    grid2 = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
    expected = 2
    return expected, grid1, grid2


@app.cell
def _(Solution, grid1, grid2, run_count_sub_islands):
    result = run_count_sub_islands(Solution, grid1, grid2)
    result
    return (result,)


@app.cell
def _(assert_count_sub_islands, expected, result):
    assert_count_sub_islands(result, expected)
    return


if __name__ == "__main__":
    app.run()
