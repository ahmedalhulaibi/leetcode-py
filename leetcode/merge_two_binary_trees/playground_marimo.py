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
    # 617. Merge Two Binary Trees

    **Easy** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    You are given two binary trees `root1` and `root2`.

    Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

    Return *the merged tree*.

    **Note:** The merging process must start from the root nodes of both trees.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/02/05/merge.jpg)

    ```
    Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
    Output: [3,4,5,5,4,null,7]
    ```

    ```
    Input: root1 = [1], root2 = [1,2]
    Output: [2,2]
    ```

    ## Constraints

    - The number of nodes in both trees is in the range [0, 2000].
    - -10^4 <= Node.val <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def merge_trees(self, root1: TreeNode[int] | None, root2: TreeNode[int] | None) -> TreeNode[int] | None:
            raise NotImplementedError('Implement merge_trees')

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
