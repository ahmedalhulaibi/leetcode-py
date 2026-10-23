import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_intersect, run_intersect
    from solution import Solution

    return Solution, assert_intersect, run_intersect


@app.cell
def _():
    # Example test case (each grid is turned into a quad-tree by the helper)
    grid1 = [[0, 1], [1, 0]]
    grid2 = [[1, 0], [0, 1]]
    expected = [[1, 1], [1, 1]]
    return expected, grid1, grid2


@app.cell
def _(Solution, grid1, grid2, run_intersect):
    result = run_intersect(Solution, grid1, grid2)
    result
    return (result,)


@app.cell
def _(assert_intersect, expected, result):
    assert_intersect(result, expected)
    return


if __name__ == "__main__":
    app.run()
