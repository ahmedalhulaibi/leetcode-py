import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_k_lists, run_merge_k_lists
    from solution import Solution

    from leetcode_py import ListNode

    return ListNode, Solution, assert_merge_k_lists, run_merge_k_lists


@app.cell
def _():
    # Example test case
    lists_data = [[1, 4, 5], [1, 3, 4], [2, 6]]
    expected_data = [1, 1, 2, 3, 4, 4, 5, 6]
    return expected_data, lists_data


@app.cell
def _(ListNode, Solution, lists_data, run_merge_k_lists):
    result = run_merge_k_lists(Solution, lists_data)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_merge_k_lists, expected_data, result):
    assert_merge_k_lists(result, expected_data)
    return


if __name__ == "__main__":
    app.run()
