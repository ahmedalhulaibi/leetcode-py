import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_same_tree, run_is_same_tree
    from solution import Solution

    return Solution, assert_is_same_tree, run_is_same_tree


@app.cell
def _():
    # Example test case
    p_list: list[int | None] = [1, 2, 3]
    q_list: list[int | None] = [1, 2, 3]
    expected = True
    return expected, p_list, q_list


@app.cell
def _(
    Solution,
    p_list: list[int | None],
    q_list: list[int | None],
    run_is_same_tree,
):
    result = run_is_same_tree(Solution, p_list, q_list)
    result
    return (result,)


@app.cell
def _(assert_is_same_tree, expected, result):
    assert_is_same_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
