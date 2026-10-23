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
    # 889. Construct Binary Tree from Preorder and Postorder Traversal

    **Medium** · Array, Hash Table, Divide and Conquer, Tree, Binary Tree

    Given two integer arrays, <code>preorder</code> and <code>postorder</code> where <code>preorder</code> is the preorder traversal of a binary tree of <strong>distinct</strong> values and <code>postorder</code> is the postorder traversal of the same tree, reconstruct and return the binary tree.</p>

    <p>If there exist multiple answers, you can return <strong>any</strong> of them.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg)

    ```
    Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
    Output: [1,2,3,4,5,6,7]
    ```

    ```
    Input: preorder = [1], postorder = [1]
    Output: [1]
    ```

    ## Constraints

    - 1 <= preorder.length <= 30
    - 1 <= preorder[i] <= preorder.length
    - All the values of preorder are unique.
    - postorder.length == preorder.length
    - 1 <= postorder[i] <= postorder.length
    - All the values of postorder are unique.
    - It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def construct_from_pre_post(self, preorder: list[int], postorder: list[int]) -> TreeNode[int] | None:
            raise NotImplementedError('Implement construct_from_pre_post')

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
