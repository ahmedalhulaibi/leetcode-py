import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_del_nodes, run_del_nodes
    from solution import Solution

    return Solution, assert_del_nodes, run_del_nodes


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4, 5, 6, 7]
    to_delete = [3, 5]
    expected_forest = [[1, 2, None, 4], [6], [7]]
    return expected_forest, root_list, to_delete


@app.cell
def _(Solution, root_list: list[int | None], run_del_nodes, to_delete):
    result = run_del_nodes(Solution, root_list, to_delete)
    result
    return (result,)


@app.cell
def _(assert_del_nodes, expected_forest, result):
    assert_del_nodes(result, expected_forest)
    return


if __name__ == "__main__":
    app.run()
