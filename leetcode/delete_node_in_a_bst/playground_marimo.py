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
    # 450. Delete Node in a BST

    **Medium** · Tree, Binary Search Tree, Binary Tree

    Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return _the **root node reference** (possibly updated) of the BST_.

    Basically, the deletion can be divided into two stages:

    1. Search for a node to remove.
    2. If the node is found, delete the node.

    Note: When a node with two children is deleted, replacing it with either its inorder successor or predecessor is accepted.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg)

    ```
    Input: root = [5,3,6,2,4,null,7], key = 3
    Output: [5,4,6,2,null,null,7]
    Explanation: One valid answer is [5,4,6,2,null,null,7]; [5,2,6,null,4,null,7] is also accepted.
    ```

    ```
    Input: root = [5,3,6,2,4,null,7], key = 0
    Output: [5,3,6,2,4,null,7]
    Explanation: The tree does not contain a node with value = 0.
    ```

    ```
    Input: root = [], key = 0
    Output: []
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [0, 10^4].
    - -10^5 <= Node.val <= 10^5
    - Each node has a unique value.
    - `root` is a valid binary search tree.
    - -10^5 <= key <= 10^5

    **Follow up:** Could you solve it with time complexity O(height of tree)?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def delete_node(self, root: TreeNode[int] | None, key: int) -> TreeNode[int] | None:
            raise NotImplementedError('Implement delete_node')

    practice_exports = {'TreeNode': TreeNode, 'Solution': Solution}
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
