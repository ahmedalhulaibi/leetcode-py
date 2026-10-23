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
    # 199. Binary Tree Right Side View

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

    ```
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)

    ```
    Input: root = [1,2,3,4,null,null,null,5]
    Output: [1,3,4,5]
    ```

    ```
    Input: root = [1,null,3]
    Output: [1,3]
    ```

    ```
    Input: root = []
    Output: []
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def right_side_view(self, root: TreeNode[int] | None) -> list[int]:
            raise NotImplementedError('Implement right_side_view')

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
