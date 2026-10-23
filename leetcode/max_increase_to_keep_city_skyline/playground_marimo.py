import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_increase_keeping_skyline, run_max_increase_keeping_skyline
    from solution import Solution

    return (
        Solution,
        assert_max_increase_keeping_skyline,
        run_max_increase_keeping_skyline,
    )


@app.cell
def _():
    # Example test case
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    expected = 35
    return expected, grid


@app.cell
def _(Solution, grid, run_max_increase_keeping_skyline):
    result = run_max_increase_keeping_skyline(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_max_increase_keeping_skyline, expected, result):
    assert_max_increase_keeping_skyline(result, expected)
    return


if __name__ == "__main__":
    app.run()
