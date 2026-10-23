import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_nodes, run_remove_nodes
    from solution import Solution

    from leetcode_py import ListNode

    return ListNode, Solution, assert_remove_nodes, run_remove_nodes


@app.cell
def _():
    # Example test case
    head_vals: list[int] = [5, 2, 13, 3, 8]
    expected_vals: list[int] = [13, 8]
    return expected_vals, head_vals


@app.cell
def _(ListNode, Solution, head_vals: list[int], run_remove_nodes):
    result = run_remove_nodes(Solution, head_vals)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_remove_nodes, expected_vals: list[int], result):
    assert_remove_nodes(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
