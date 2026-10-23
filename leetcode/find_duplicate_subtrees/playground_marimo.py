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
    # 652. Find Duplicate Subtrees

    **Medium** · Hash Table, Tree, Depth-First Search, Binary Tree

    Given the `root` of a binary tree, return all **duplicate subtrees**.

    For each kind of duplicate subtrees, you only need to return the root node of any one **of them**.

    Two trees are **duplicate** if they have the **same structure** with the **same node values**.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/08/16/e1.jpg)

    ```
    Input: root = [1,2,3,4,null,2,4,null,null,4]
    Output: [[2,4],[4]]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/08/16/e2.jpg)

    ```
    Input: root = [2,1,1]
    Output: [[1]]
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2020/08/16/e33.jpg)

    ```
    Input: root = [2,2,2,3,null,3,null]
    Output: [[2,3],[3]]
    ```

    ## Constraints

    - The number of the nodes in the tree will be in the range [1, 5000]
    - -200 <= Node.val <= 200



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import Counter
    from leetcode_py import TreeNode

    class Solution:

        def find_duplicate_subtrees(self, root: TreeNode[int] | None) -> list[TreeNode[int] | None]:
            raise NotImplementedError('Implement find_duplicate_subtrees')

    practice_exports = {'Counter': Counter, 'TreeNode': TreeNode, 'Solution': Solution}
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
