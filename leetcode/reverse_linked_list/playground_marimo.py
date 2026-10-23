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
    # 206. Reverse Linked List

    **Easy** · Linked List, Recursion

    Given the `head` of a singly linked list, reverse the list, and return the reversed list.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

    ```
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

    ```
    Input: head = [1,2]
    Output: [2,1]
    ```

    ```
    Input: head = []
    Output: []
    ```

    ## Constraints

    - The number of nodes in the list is the range `[0, 5000]`.
    - `-5000 <= Node.val <= 5000`

    **Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def reverse_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement reverse_list')

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
