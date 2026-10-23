import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_maximum_gold, run_get_maximum_gold
    from solution import Solution

    return Solution, assert_get_maximum_gold, run_get_maximum_gold


@app.cell
def _():
    # Example test case
    grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    expected = 24
    return expected, grid


@app.cell
def _(Solution, grid, run_get_maximum_gold):
    result = run_get_maximum_gold(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_get_maximum_gold, expected, result):
    assert_get_maximum_gold(result, expected)
    return


if __name__ == "__main__":
    app.run()
