# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 445. Add Two Numbers II

    **Medium** · Linked List, Math, Stack

    You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number `0` itself.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg)

    ```
    Input: l1 = [7,2,4,3], l2 = [5,6,4]
    Output: [7,8,0,7]
    ```

    ```
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [8,0,7]
    ```

    ```
    Input: l1 = [0], l2 = [0]
    Output: [0]
    ```

    ## Constraints

    - The number of nodes in each linked list is in the range `[1, 100]`.
    - `0 <= Node.val <= 9`
    - It is guaranteed that the list represents a number that does not have leading zeros.

    **Follow up:** Could you solve it without reversing the input lists?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def add_two_numbers(self, l1: ListNode[int] | None, l2: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement add_two_numbers')

    practice_exports = {'ListNode': ListNode, 'Solution': Solution}
    return (practice_exports,)


@app.cell(hide_code=True)
def _(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def _(mo, practice_exports, run_practice_tests, run_tests):
    mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))
    test_result = run_practice_tests(mo.notebook_dir(), practice_exports)
    mo.vstack([
        mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "
              f"{test_result.skipped} skipped**"),
        mo.md("**All tests passed.**" if test_result.exit_code == 0 else "**Tests are not passing yet.**"),
        mo.accordion({"Test output": mo.plain_text(test_result.output)}),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
