import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_trees, run_merge_trees
    from solution import Solution

    return Solution, assert_merge_trees, run_merge_trees


@app.cell
def _():
    # Example test case
    root1_list: list[int | None] = [1, 3, 2, 5]
    root2_list: list[int | None] = [2, 1, 3, None, 4, None, 7]
    expected: list[int | None] = [3, 4, 5, 5, 4, None, 7]
    return expected, root1_list, root2_list


@app.cell
def _(
    Solution,
    root1_list: list[int | None],
    root2_list: list[int | None],
    run_merge_trees,
):
    result = run_merge_trees(Solution, root1_list, root2_list)
    result
    return (result,)


@app.cell
def _(assert_merge_trees, expected: list[int | None], result):
    assert_merge_trees(result, expected)
    return


if __name__ == "__main__":
    app.run()
