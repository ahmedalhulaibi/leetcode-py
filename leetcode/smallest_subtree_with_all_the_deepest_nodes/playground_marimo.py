import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subtree_with_all_deepest, run_subtree_with_all_deepest
    from solution import Solution

    return (
        Solution,
        assert_subtree_with_all_deepest,
        run_subtree_with_all_deepest,
    )


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    expected_list: list[int | None] = [2, 7, 4]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_subtree_with_all_deepest):
    result = run_subtree_with_all_deepest(Solution, root_list)
    result
    return (result,)


@app.cell
def _(
    assert_subtree_with_all_deepest,
    expected_list: list[int | None],
    result,
):
    assert_subtree_with_all_deepest(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
