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
    # 156. Binary Tree Upside Down

    **Medium** · Tree, Depth-First Search, Binary Tree

    Given the `root` of a binary tree, turn the tree upside down and return the new root.

    You can turn a binary tree upside down with the following steps:

    1. The original left child becomes the new root.
    2. The original root becomes the new right child.
    3. The original right child becomes the new left child.

    The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node that shares the same parent) and has no children.

    ## Examples

    ```
    Input: root = [1,2,3,4,5]
    Output: [4,5,2,null,null,3,1]
    ```

    ```
    Input: root = []
    Output: []
    ```

    ```
    Input: root = [1]
    Output: [1]
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [0, 10]
    - 1 <= Node.val <= 10
    - Every right node in the tree has a sibling (a left node that shares the same parent)
    - Every right node in the tree has no children



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def upside_down_binary_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
            raise NotImplementedError('Implement upside_down_binary_tree')

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
