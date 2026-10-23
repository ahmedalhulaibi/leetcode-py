import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_validate_binary_tree_nodes, run_validate_binary_tree_nodes
    from solution import Solution

    return (
        Solution,
        assert_validate_binary_tree_nodes,
        run_validate_binary_tree_nodes,
    )


@app.cell
def _():
    # Example test case
    n = 4
    left_child = [1, -1, 3, -1]
    right_child = [2, -1, -1, -1]
    expected = True
    return expected, left_child, n, right_child


@app.cell
def _(Solution, left_child, n, right_child, run_validate_binary_tree_nodes):
    result = run_validate_binary_tree_nodes(Solution, n, left_child, right_child)
    result
    return (result,)


@app.cell
def _(assert_validate_binary_tree_nodes, expected, result):
    assert_validate_binary_tree_nodes(result, expected)
    return


if __name__ == "__main__":
    app.run()
