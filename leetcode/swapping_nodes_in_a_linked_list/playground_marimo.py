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
    # 1721. Swapping Nodes in a Linked List

    **Medium** · Linked List, Two Pointers

    You are given the `head` of a linked list, and an integer `k`.

    Return *the head of the linked list after **swapping** the values of the `k<sup>th</sup>` node from the beginning and the `k<sup>th</sup>` node from the end (the list is **1-indexed**)*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg)

    ```
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]
    ```

    ```
    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]
    ```

    ## Constraints

    - The number of nodes in the list is `n`.
    - `1 <= k <= n <= 10^5`
    - `0 <= Node.val <= 100`

    **Follow up:** Could you do this in one pass?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def swap_nodes(self, head: ListNode[int] | None, k: int) -> ListNode[int] | None:
            raise NotImplementedError('Implement swap_nodes')

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
