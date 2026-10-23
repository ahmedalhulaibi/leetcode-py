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
    # 25. Reverse Nodes in k-Group

    **Hard** · Linked List, Recursion

    Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.

    `k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

    ```
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

    ```
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
    ```

    ## Constraints

    - The number of nodes in the list is n.
    - 1 <= k <= n <= 5000
    - 0 <= Node.val <= 1000

    **Follow-up:** Can you solve the problem in `O(1)` extra memory space?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def reverse_k_group(self, head: ListNode[int] | None, k: int) -> ListNode[int] | None:
            raise NotImplementedError('Implement reverse_k_group')

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
