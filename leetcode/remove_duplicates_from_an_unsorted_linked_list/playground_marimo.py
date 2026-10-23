import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_delete_duplicates_unsorted, run_delete_duplicates_unsorted
    from solution import Solution

    from leetcode_py import ListNode

    return (
        ListNode,
        Solution,
        assert_delete_duplicates_unsorted,
        run_delete_duplicates_unsorted,
    )


@app.cell
def _():
    # Example test case
    head_vals = [1, 2, 3, 2]
    expected_vals = [1, 3]
    return expected_vals, head_vals


@app.cell
def _(ListNode, Solution, head_vals, run_delete_duplicates_unsorted):
    result = run_delete_duplicates_unsorted(Solution, head_vals)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_delete_duplicates_unsorted, expected_vals, result):
    assert_delete_duplicates_unsorted(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
