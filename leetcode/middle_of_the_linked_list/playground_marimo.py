import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_middle_node, run_middle_node
    from solution import Solution

    from leetcode_py import ListNode

    return ListNode, Solution, assert_middle_node, run_middle_node


@app.cell
def _():
    # Example test case
    head_list = [1, 2, 3, 4, 5]
    expected_list = [3, 4, 5]
    return expected_list, head_list


@app.cell
def _(ListNode, Solution, head_list, run_middle_node):
    result = run_middle_node(Solution, head_list)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_middle_node, expected_list, result):
    assert_middle_node(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
