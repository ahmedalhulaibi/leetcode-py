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
    # 669. Trim a Binary Search Tree

    **Medium** · Tree, Depth-First Search, Binary Search Tree, Binary Tree

    Given the root of a binary search tree and the lowest and highest boundaries as `low` and `high`, trim the tree so that all its elements lies in `[low, high]`. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

    Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg)

    ```
    Input: root = [1,0,2], low = 1, high = 2
    Output: [1,null,2]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg)

    ```
    Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
    Output: [3,2,null,1]
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 10^4].
    - 0 <= Node.val <= 10^4
    - The value of each node in the tree is unique.
    - root is guaranteed to be a valid binary search tree.
    - 0 <= low <= high <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def trim_bst(self, root: TreeNode[int] | None, low: int, high: int) -> TreeNode[int] | None:
            raise NotImplementedError('Implement trim_bst')

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
