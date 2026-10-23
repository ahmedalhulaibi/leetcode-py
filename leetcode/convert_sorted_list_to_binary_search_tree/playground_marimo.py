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
    # 109. Convert Sorted List to Binary Search Tree

    **Medium** · Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree

    Given the `head` of a singly linked list where elements are sorted in **ascending order**, convert it to a **height-balanced** binary search tree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)

    ```
    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
    ```

    ```
    Input: head = []
    Output: []
    ```

    ## Constraints

    - The number of nodes in head is in the range [0, 2 * 10^4].
    - -10^5 <= Node.val <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode, TreeNode

    class Solution:

        def sorted_list_to_bst(self, head: ListNode[int] | None) -> TreeNode[int] | None:
            raise NotImplementedError('Implement sorted_list_to_bst')

    practice_exports = {'ListNode': ListNode, 'TreeNode': TreeNode, 'Solution': Solution}
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
