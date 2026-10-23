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
    # 872. Leaf-Similar Trees

    **Easy** · Tree, Depth-First Search, Binary Tree

    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a <strong>leaf value sequence</strong>.</p>

    <p>For example, in the given tree above, the leaf value sequence is <code>(6, 7, 4, 9, 8)</code>.</p>

    <p>Two binary trees are considered <em>leaf-similar</em> if their leaf value sequence is the same.</p>

    <p>Return <code>true</code> if and only if the two given trees with head nodes <code>root1</code> and <code>root2</code> are leaf-similar.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)

    ```
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)

    ```
    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false
    ```

    ## Constraints

    - The number of nodes in each tree will be in the range [1, 200].
    - Both of the given trees will have values in the range [0, 200].



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def leaf_similar(self, root1: TreeNode[int] | None, root2: TreeNode[int] | None) -> bool:
            raise NotImplementedError('Implement leaf_similar')

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
