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
    # 110. Balanced Binary Tree

    **Easy** · Tree, Depth-First Search, Binary Tree

    Given a binary tree, determine if it is **height-balanced**.

    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

    ```
    Input: root = [3,9,20,null,null,15,7]
    Output: true
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

    ```
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false
    ```

    ```
    Input: root = []
    Output: true
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 5000]`.
    - `-10^4 <= Node.val <= 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def is_balanced(self, root: TreeNode[int] | None) -> bool:
            raise NotImplementedError('Implement is_balanced')

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
