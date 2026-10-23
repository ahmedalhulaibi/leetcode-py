import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_two_lists, run_merge_two_lists
    from solution import Solution

    from leetcode_py import ListNode

    return ListNode, Solution, assert_merge_two_lists, run_merge_two_lists


@app.cell
def _():
    # Example test case
    list1_vals = [1, 2, 4]
    list2_vals = [1, 3, 4]
    expected_vals = [1, 1, 2, 3, 4, 4]
    return expected_vals, list1_vals, list2_vals


@app.cell
def _(ListNode, Solution, list1_vals, list2_vals, run_merge_two_lists):
    result = run_merge_two_lists(Solution, list1_vals, list2_vals)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_merge_two_lists, expected_vals, result):
    assert_merge_two_lists(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
