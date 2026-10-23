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
    # 968. Binary Tree Cameras

    **Hard** · Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees

    You are given the `root` of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

    Return the minimum number of cameras needed to monitor all nodes of the tree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png)

    ```
    Input: root = [0,0,null,0,0]
    Output: 1
    Explanation: One camera is enough to monitor all nodes if placed as shown.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png)

    ```
    Input: root = [0,0,null,0,null,0,null,null,0]
    Output: 2
    Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 1000]
    - Node.val == 0



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def min_camera_cover(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement min_camera_cover')

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
