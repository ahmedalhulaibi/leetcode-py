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
    # 1110. Delete Nodes And Return Forest

    **Medium** · Array, Hash Table, Tree, Depth-First Search, Binary Tree

    Given the <code>root</code> of a binary tree, each node in the tree has a <strong>distinct</strong> value.

    After deleting all nodes with a value in <code>to_delete</code>, we are left with a forest (a&nbsp;disjoint union of trees).

    Return the roots of the trees in the remaining forest. You may return them in any order.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png)

    ```
    Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    Output: [[1,2,null,4],[6],[7]]
    ```

    ```
    Input: root = [1,2,4,null,3], to_delete = [3]
    Output: [[1,2,4]]
    ```

    ## Constraints

    - The number of nodes in the given tree is at most <code>1000</code>.
    - Each node has a <strong>distinct</strong> value between <code>1</code> and <code>1000</code>.
    - <code>to_delete.length &lt;= 1000</code>
    - <code>to_delete</code> contains distinct values between <code>1</code> and <code>1000</code>.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def del_nodes(self, root: TreeNode[int] | None, to_delete: list[int]) -> list[TreeNode[int]]:
            raise NotImplementedError('Implement del_nodes')

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
