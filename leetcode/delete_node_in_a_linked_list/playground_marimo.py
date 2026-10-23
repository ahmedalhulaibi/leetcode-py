import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_delete_node, run_delete_node
    from solution import Solution

    return Solution, assert_delete_node, run_delete_node


@app.cell
def _():
    # Example test case
    head_list: list[int] = [4, 5, 1, 9]
    node_val = 5
    expected_list = [4, 1, 9]
    return expected_list, head_list, node_val


@app.cell
def _(Solution, head_list: list[int], node_val, run_delete_node):
    result = run_delete_node(Solution, head_list, node_val)
    result
    return (result,)


@app.cell
def _(assert_delete_node, expected_list, result):
    assert_delete_node(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
