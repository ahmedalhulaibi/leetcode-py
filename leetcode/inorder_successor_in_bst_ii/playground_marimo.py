import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_inorder_successor, run_inorder_successor
    from solution import Solution

    return Solution, assert_inorder_successor, run_inorder_successor


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [2, 1, 3]
    node_val = 1
    expected_val = 2
    return expected_val, node_val, root_list


@app.cell
def _(Solution, node_val, root_list: list[int | None], run_inorder_successor):
    result = run_inorder_successor(Solution, root_list, node_val)
    result
    return (result,)


@app.cell
def _(assert_inorder_successor, expected_val, result):
    assert_inorder_successor(result, expected_val)
    return


if __name__ == "__main__":
    app.run()
