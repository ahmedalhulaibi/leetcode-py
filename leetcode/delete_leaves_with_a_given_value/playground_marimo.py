import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_leaf_nodes, run_remove_leaf_nodes
    from solution import Solution

    return Solution, assert_remove_leaf_nodes, run_remove_leaf_nodes


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 2, None, 2, 4]
    target = 2
    expected_list: list[int | None] = [1, None, 3, None, 4]
    return expected_list, root_list, target


@app.cell
def _(Solution, root_list: list[int | None], run_remove_leaf_nodes, target):
    result = run_remove_leaf_nodes(Solution, root_list, target)
    result
    return (result,)


@app.cell
def _(assert_remove_leaf_nodes, expected_list: list[int | None], result):
    assert_remove_leaf_nodes(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
