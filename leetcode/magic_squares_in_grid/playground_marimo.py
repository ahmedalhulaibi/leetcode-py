import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_magic_squares_inside, run_num_magic_squares_inside
    from solution import Solution

    return (
        Solution,
        assert_num_magic_squares_inside,
        run_num_magic_squares_inside,
    )


@app.cell
def _():
    # Example test case
    grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
    expected = 1
    return expected, grid


@app.cell
def _(Solution, grid, run_num_magic_squares_inside):
    result = run_num_magic_squares_inside(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_num_magic_squares_inside, expected, result):
    assert_num_magic_squares_inside(result, expected)
    return


if __name__ == "__main__":
    app.run()
