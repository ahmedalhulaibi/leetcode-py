import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_leaf_similar, run_leaf_similar
    from solution import Solution

    return Solution, assert_leaf_similar, run_leaf_similar


@app.cell
def _():
    # Example test case
    root1_list: list[int | None] = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2_list: list[int | None] = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    expected = True
    return expected, root1_list, root2_list


@app.cell
def _(
    Solution,
    root1_list: list[int | None],
    root2_list: list[int | None],
    run_leaf_similar,
):
    result = run_leaf_similar(Solution, root1_list, root2_list)
    result
    return (result,)


@app.cell
def _(assert_leaf_similar, expected, result):
    assert_leaf_similar(result, expected)
    return


if __name__ == "__main__":
    app.run()
