import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_corner_rectangles, run_count_corner_rectangles
    from solution import Solution

    return (
        Solution,
        assert_count_corner_rectangles,
        run_count_corner_rectangles,
    )


@app.cell
def _():
    # Example test case
    grid = [[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]
    expected = 1
    return expected, grid


@app.cell
def _(Solution, grid, run_count_corner_rectangles):
    result = run_count_corner_rectangles(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_count_corner_rectangles, expected, result):
    assert_count_corner_rectangles(result, expected)
    return


if __name__ == "__main__":
    app.run()
