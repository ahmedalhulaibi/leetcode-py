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
    # 19. Remove Nth Node From End of List

    **Medium** · Linked List, Two Pointers

    Given the `head` of a linked list, remove the `n<sup>th</sup>` node from the end of the list and return its head.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

    ```
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    ```

    ```
    Input: head = [1], n = 1
    Output: []
    ```

    ```
    Input: head = [1,2], n = 1
    Output: [1]
    ```

    ## Constraints

    - The number of nodes in the list is `sz`.
    - `1 <= sz <= 30`
    - `0 <= Node.val <= 100`
    - `1 <= n <= sz`

    **Follow up:** Could you do this in one pass?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def remove_nth_from_end(self, head: ListNode[int] | None, n: int) -> ListNode[int] | None:
            raise NotImplementedError('Implement remove_nth_from_end')

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
