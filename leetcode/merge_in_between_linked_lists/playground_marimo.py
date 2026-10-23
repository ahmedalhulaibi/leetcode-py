import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_in_between, run_merge_in_between
    from solution import Solution

    from leetcode_py import ListNode

    return ListNode, Solution, assert_merge_in_between, run_merge_in_between


@app.cell
def _():
    # Example test case
    list1_vals = [10, 1, 13, 6, 9, 5]
    a = 3
    b = 4
    list2_vals = [1000000, 1000001, 1000002]
    expected_vals = [10, 1, 13, 1000000, 1000001, 1000002, 5]
    return a, b, expected_vals, list1_vals, list2_vals


@app.cell
def _(ListNode, Solution, a, b, list1_vals, list2_vals, run_merge_in_between):
    result = run_merge_in_between(Solution, list1_vals, a, b, list2_vals)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_merge_in_between, expected_vals, result):
    assert_merge_in_between(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
