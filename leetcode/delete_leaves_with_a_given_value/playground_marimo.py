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
    # 1325. Delete Leaves With a Given Value

    **Medium** · Tree, Depth-First Search, Binary Tree

    Given a binary tree `root` and an integer `target`, delete all the **leaf nodes** with value `target`.

    Note that once you delete a leaf node with value `target`, if its parent node becomes a leaf node and has the value `target`, it should also be deleted (you need to continue doing that until you cannot).

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/01/09/sample_1_1684.png)

    ```
    Input: root = [1,2,3,2,null,2,4], target = 2
    Output: [1,null,3,null,4]
    Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
    After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/01/09/sample_2_1684.png)

    ```
    Input: root = [1,3,3,3,2], target = 3
    Output: [1,3,null,null,2]
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2020/01/15/sample_3_1684.png)

    ```
    Input: root = [1,2,null,2,null,2], target = 2
    Output: [1]
    Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 3000]`
    - `1 <= Node.val, target <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def remove_leaf_nodes(self, root: TreeNode[int] | None, target: int) -> TreeNode[int] | None:
            raise NotImplementedError('Implement remove_leaf_nodes')

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
