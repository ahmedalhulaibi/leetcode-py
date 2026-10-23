import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_cut_off_tree, run_cut_off_tree
    from solution import Solution

    return Solution, assert_cut_off_tree, run_cut_off_tree


@app.cell
def _():
    # Example test case
    forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
    expected = 6
    return expected, forest


@app.cell
def _(Solution, forest, run_cut_off_tree):
    result = run_cut_off_tree(Solution, forest)
    result
    return (result,)


@app.cell
def _(assert_cut_off_tree, expected, result):
    assert_cut_off_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
