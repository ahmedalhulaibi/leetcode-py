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
    # 328. Odd Even Linked List

    **Medium** · Linked List

    Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

    The **first** node is considered **odd**, and the **second** node is **even**, and so on.

    Note that the relative order inside both the even and odd groups should remain as it was in the input.

    You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)

    ```
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)

    ```
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]
    ```

    ## Constraints

    - The number of nodes in the linked list is in the range [0, 10^4]
    - -10^6 <= Node.val <= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def odd_even_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement odd_even_list')

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
