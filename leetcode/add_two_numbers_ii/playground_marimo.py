import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_two_numbers, run_add_two_numbers
    from solution import Solution

    from leetcode_py import ListNode

    return ListNode, Solution, assert_add_two_numbers, run_add_two_numbers


@app.cell
def _():
    # Example test case
    l1_vals = [7, 2, 4, 3]
    l2_vals = [5, 6, 4]
    expected_vals = [7, 8, 0, 7]
    return expected_vals, l1_vals, l2_vals


@app.cell
def _(ListNode, Solution, l1_vals, l2_vals, run_add_two_numbers):
    result = run_add_two_numbers(Solution, l1_vals, l2_vals)
    ListNode[int].to_list(result) if result else []
    return (result,)


@app.cell
def _(assert_add_two_numbers, expected_vals, result):
    assert_add_two_numbers(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
