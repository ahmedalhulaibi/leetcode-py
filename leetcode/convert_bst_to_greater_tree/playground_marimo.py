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
    # 538. Convert BST to Greater Tree

    **Medium** · Tree, Depth-First Search, Binary Search Tree, Binary Tree

    Given the `root` of a Binary Search Tree (BST), convert it to a **Greater Tree** such that every key of the original BST is changed to the original key plus the sum of all keys **greater** than the original key in BST.

    As a reminder, a *binary search tree* is a tree that satisfies these constraints:

    - The left subtree of a node contains only nodes with keys **less than** the node's key.
    - The right subtree of a node contains only nodes with keys **greater than** the node's key.
    - Both the left and right subtrees must also be binary search trees.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/05/02/tree.png)

    ```
    Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
    ```

    ```
    Input: root = [0,null,1]
    Output: [1,null,1]
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `-10^4 <= Node.val <= 10^4`
    - All the values in the tree are **unique**.
    - `root` is guaranteed to be a valid binary search tree.

    **Note:** This question is the same as 1038: Binary Search Tree to Greater Sum Tree.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def convert_bst(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
            raise NotImplementedError('Implement convert_bst')

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
