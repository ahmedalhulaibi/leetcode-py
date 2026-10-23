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
    # 98. Validate Binary Search Tree

    **Medium** · Tree, Depth-First Search, Binary Search Tree, Binary Tree

    Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

    A **valid BST** is defined as follows:

    - The left subtree of a node contains only nodes with keys **strictly less than** the node's key.
    - The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
    - Both the left and right subtrees must also be binary search trees.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

    ```
    Input: root = [2,1,3]
    Output: true
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

    ```
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    ```
    **Explanation:** The root node's value is 5 but its right child's value is 4.

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-2^31 <= Node.val <= 2^31 - 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def is_valid_bst(self, root: TreeNode[int] | None) -> bool:
            raise NotImplementedError('Implement is_valid_bst')

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
