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
    # 141. Linked List Cycle

    **Easy** · Hash Table, Linked List, Two Pointers

    Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

    Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

    ```
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    ```
    **Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

    ![Example 2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

    ```
    Input: head = [1,2], pos = 0
    Output: true
    ```
    **Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

    ![Example 3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

    ```
    Input: head = [1], pos = -1
    Output: false
    ```
    **Explanation:** There is no cycle in the linked list.

    ## Constraints

    - The number of the nodes in the list is in the range `[0, 10^4]`.
    - `-10^5 <= Node.val <= 10^5`
    - `pos` is `-1` or a **valid index** in the linked-list.

    **Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def has_cycle(self, head: ListNode[int] | None) -> bool:
            raise NotImplementedError('Implement has_cycle')

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
