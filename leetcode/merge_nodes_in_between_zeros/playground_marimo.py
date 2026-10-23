import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_nodes, run_merge_nodes
    from solution import Solution

    from leetcode_py import ListNode

    return ListNode, Solution, assert_merge_nodes, run_merge_nodes


@app.cell
def _():
    # Example test case
    head_vals: list[int] = [0, 3, 1, 0, 4, 5, 2, 0]
    expected_vals: list[int] = [4, 11]
    return expected_vals, head_vals


@app.cell
def _(ListNode, Solution, head_vals: list[int], run_merge_nodes):
    result = run_merge_nodes(Solution, head_vals)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_merge_nodes, expected_vals: list[int], result):
    assert_merge_nodes(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
