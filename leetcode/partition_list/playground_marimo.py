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
    # 86. Partition List

    **Medium** · Linked List, Two Pointers

    Given the `head` of a linked list and a value `x`, partition it such that all nodes **less than** `x` come before nodes **greater than or equal** to `x`.

    You should **preserve** the original relative order of the nodes in each of the two partitions.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)

    ```
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
    ```

    ```
    Input: head = [2,1], x = 2
    Output: [1,2]
    ```

    ## Constraints

    - The number of nodes in the list is in the range `[0, 200]`.
    - `-100 <= Node.val <= 100`
    - `-200 <= x <= 200`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def partition(self, head: ListNode[int] | None, x: int) -> ListNode[int] | None:
            raise NotImplementedError('Implement partition')

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
