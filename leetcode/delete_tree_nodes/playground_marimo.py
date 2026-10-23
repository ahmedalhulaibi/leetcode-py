import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_delete_tree_nodes, run_delete_tree_nodes
    from solution import Solution

    return Solution, assert_delete_tree_nodes, run_delete_tree_nodes


@app.cell
def _():
    # Example test case
    nodes = 7
    parent = [-1, 0, 0, 1, 2, 2, 2]
    value = [1, -2, 4, 0, -2, -1, -1]
    expected = 2
    return expected, nodes, parent, value


@app.cell
def _(Solution, nodes, parent, run_delete_tree_nodes, value):
    result = run_delete_tree_nodes(Solution, nodes, parent, value)
    result
    return (result,)


@app.cell
def _(assert_delete_tree_nodes, expected, result):
    assert_delete_tree_nodes(result, expected)
    return


if __name__ == "__main__":
    app.run()
