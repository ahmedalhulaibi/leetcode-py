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
    # 501. Find Mode in Binary Search Tree

    **Easy** · Tree, Depth-First Search, Binary Search Tree, Binary Tree

    Given the `root` of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

    If the tree has more than one mode, return them in **any order**.

    Assume a BST is defined as follows:

    - The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
    - The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
    - Both the left and right subtrees must also be binary search trees.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg)

    ```
    Input: root = [1,null,2,2]
    Output: [2]
    ```

    ```
    Input: root = [0]
    Output: [0]
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-10^5 <= Node.val <= 10^5`

    **Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count.)

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def find_mode(self, root: TreeNode[int] | None) -> list[int]:
            raise NotImplementedError('Implement find_mode')

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
