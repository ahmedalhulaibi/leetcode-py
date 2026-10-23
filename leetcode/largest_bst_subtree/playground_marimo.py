import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_bst_subtree, run_largest_bst_subtree
    from solution import Solution

    return Solution, assert_largest_bst_subtree, run_largest_bst_subtree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [10, 5, 15, 1, 8, None, 7]
    expected = 3
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_largest_bst_subtree):
    result = run_largest_bst_subtree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_largest_bst_subtree, expected, result):
    assert_largest_bst_subtree(result, expected)
    return


if __name__ == "__main__":
    app.run()
