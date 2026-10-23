import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_subtree, run_is_subtree
    from solution import Solution

    return Solution, assert_is_subtree, run_is_subtree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 4, 5, 1, 2]
    sub_root_list: list[int | None] = [4, 1, 2]
    expected = True
    return expected, root_list, sub_root_list


@app.cell
def _(
    Solution,
    root_list: list[int | None],
    run_is_subtree,
    sub_root_list: list[int | None],
):
    result = run_is_subtree(Solution, root_list, sub_root_list)
    result
    return (result,)


@app.cell
def _(assert_is_subtree, expected, result):
    assert_is_subtree(result, expected)
    return


if __name__ == "__main__":
    app.run()
