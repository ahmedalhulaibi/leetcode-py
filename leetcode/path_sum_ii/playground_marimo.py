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
    # 113. Path Sum II

    **Medium** · Backtracking, Tree, Depth-First Search, Binary Tree

    Given the `root` of a binary tree and an integer `targetSum`, return all **root-to-leaf** paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node **values**, not node references.

    A **root-to-leaf** path is a path starting from the root and ending at any leaf node. A **leaf** is a node with no children.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)

    ```
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]
    Explanation: There are two paths whose sum equals targetSum:
    5 + 4 + 11 + 2 = 22
    5 + 8 + 4 + 5 = 22
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

    ```
    Input: root = [1,2,3], targetSum = 5
    Output: []
    ```

    ```
    Input: root = [1,2], targetSum = 0
    Output: []
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 5000]`.
    - `-1000 <= Node.val <= 1000`
    - `-1000 <= targetSum <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def path_sum(self, root: TreeNode[int] | None, target_sum: int) -> list[list[int]]:
            raise NotImplementedError('Implement path_sum')

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
