import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_outer_trees, run_outer_trees
    from solution import Solution

    return Solution, assert_outer_trees, run_outer_trees


@app.cell
def _():
    # Example test case
    trees = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
    expected = [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]
    return expected, trees


@app.cell
def _(Solution, run_outer_trees, trees):
    result = run_outer_trees(Solution, trees)
    result
    return (result,)


@app.cell
def _(assert_outer_trees, expected, result):
    assert_outer_trees(result, expected)
    return


if __name__ == "__main__":
    app.run()
