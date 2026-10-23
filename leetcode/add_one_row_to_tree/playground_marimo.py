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
    # 623. Add One Row to Tree

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a binary tree and two integers `val` and `depth`, add a row of nodes with value `val` at the given depth `depth`.

    Note that the root node is at depth `1`.

    The adding rule is:

    - Given the integer `depth`, for each not null tree node `cur` at the depth `depth - 1`, create two tree nodes with value `val` as `cur`'s left subtree root and right subtree root.
    - `cur`'s original left subtree should be the left subtree of the new left subtree root.
    - `cur`'s original right subtree should be the right subtree of the new right subtree root.
    - If `depth == 1` that means there is no depth `depth - 1` at all, then create a tree node with value `val` as the new root of the whole original tree, and the original tree is the new root's left subtree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg)

    ```
    Input: root = [4,2,6,3,1,5], val = 1, depth = 2
    Output: [4,1,1,2,null,null,6,3,1,5]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg)

    ```
    Input: root = [4,2,null,3,1], val = 1, depth = 3
    Output: [4,2,null,1,1,3,null,null,1]
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 10^4]
    - The depth of the tree is in the range [1, 10^4]
    - -100 <= Node.val <= 100
    - -10^5 <= val <= 10^5
    - 1 <= depth <= the depth of tree + 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def add_one_row(self, root: TreeNode[int] | None, val: int, depth: int) -> TreeNode[int] | None:
            raise NotImplementedError('Implement add_one_row')

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
