import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_delete_nodes, run_delete_nodes
    from solution import Solution

    from leetcode_py import ListNode

    return ListNode, Solution, assert_delete_nodes, run_delete_nodes


@app.cell
def _():
    # Example test case
    head_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    m = 2
    n = 3
    expected_vals = [1, 2, 6, 7, 11, 12]
    return expected_vals, head_vals, m, n


@app.cell
def _(ListNode, Solution, head_vals, m, n, run_delete_nodes):
    result = run_delete_nodes(Solution, head_vals, m, n)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_delete_nodes, expected_vals, result):
    assert_delete_nodes(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
