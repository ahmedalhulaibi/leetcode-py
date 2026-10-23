import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_distinct_islands_ii, run_num_distinct_islands_ii
    from solution import Solution

    return (
        Solution,
        assert_num_distinct_islands_ii,
        run_num_distinct_islands_ii,
    )


@app.cell
def _():
    # Example test case
    grid = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]
    expected = 1
    return expected, grid


@app.cell
def _(Solution, grid, run_num_distinct_islands_ii):
    result = run_num_distinct_islands_ii(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_num_distinct_islands_ii, expected, result):
    assert_num_distinct_islands_ii(result, expected)
    return


if __name__ == "__main__":
    app.run()
