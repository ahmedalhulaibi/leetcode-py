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
    # 143. Reorder List

    **Medium** · Linked List, Two Pointers, Stack, Recursion

    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln

    *Reorder the list to be on the following form:*

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

    ```
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

    ```
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]
    ```

    ## Constraints

    - The number of nodes in the list is in the range [1, 5 * 10^4].
    - 1 <= Node.val <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def reorder_list(self, head: ListNode[int] | None) -> None:
            raise NotImplementedError('Implement reorder_list')

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
