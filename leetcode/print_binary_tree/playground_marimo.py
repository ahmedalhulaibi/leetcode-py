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
    # 655. Print Binary Tree

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a binary tree, construct a **0-indexed** `m x n` string matrix `res` that represents a **formatted layout** of the tree. The formatted layout matrix should be constructed using the following rules:

    - The **height** of the tree is `height` and the number of rows `m` should be equal to `height + 1`.
    - The number of columns `n` should be equal to `2^height+1^ - 1`.
    - Place the **root node** in the **middle** of the **top row** (more formally, at location `res[0][(n-1)/2]`).
    - For each node that has been placed in the matrix at position `res[r][c]`, place its **left child** at `res[r+1][c-2^height-r-1^]` and its **right child** at `res[r+1][c+2^height-r-1^]`.
    - Continue this process until all the nodes in the tree have been placed.
    - Any empty cells should contain the empty string `"\"`.

    Return the constructed matrix `res`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/03/print1-tree.jpg)

    ```
    Input: root = [1,2]
    Output: [['','1',''],['2','','']]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/05/03/print2-tree.jpg)

    ```
    Input: root = [1,2,3,null,4]
    Output: [['','','','1','','',''],['','2','','','','3',''],['','','4','','','','']]
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 2^10]`.
    - `-99 <= Node.val <= 99`
    - The depth of the tree will be in the range `[1, 10]`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def print_tree(self, root: TreeNode[int] | None) -> list[list[str]]:
            raise NotImplementedError('Implement print_tree')

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
