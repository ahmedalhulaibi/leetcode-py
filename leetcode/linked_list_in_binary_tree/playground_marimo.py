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
    # 1367. Linked List in Binary Tree

    **Medium** · Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given a binary tree root and a&nbsp;linked list with&nbsp;head&nbsp;as the first node.&nbsp;

    Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree&nbsp;otherwise return False.

    In this context downward path means a path that starts at some node and goes downwards.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/02/12/sample_1_1720.png)

    ```
    Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: true
    Explanation: Nodes in blue form a subpath in the binary Tree.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/02/12/sample_2_1720.png)

    ```
    Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: true
    ```

    ```
    Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: false
    Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
    ```

    ## Constraints

    - The number of nodes in the tree will be in the range [1, 2500].
    - The number of nodes in the list will be in the range [1, 100].
    - 1 <= Node.val <= 100 for each node in the linked list and binary tree.

    **Follow up:** What if you cannot modify the input lists, i.e. reversing them is not allowed?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode, TreeNode

    class Solution:

        def is_sub_path(self, head: ListNode[int] | None, root: TreeNode[int] | None) -> bool:
            raise NotImplementedError('Implement is_sub_path')

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
