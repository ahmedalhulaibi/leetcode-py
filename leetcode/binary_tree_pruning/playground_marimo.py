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
    # 814. Binary Tree Pruning

    **Medium** · Tree, Depth-First Search, Binary Tree

    Given the `root` of a binary tree, return the same tree where every subtree (of the given tree) not containing a `1` has been removed.

    A subtree of a node `node` is `node` plus every node that is a descendant of `node`.

    ## Examples

    ![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)

    ```
    Input: root = [1,null,0,0,1]
    Output: [1,null,0,null,1]
    Explanation:
    Only the red nodes satisfy the property "every subtree not containing a 1".
    The diagram on the right represents the answer.
    ```

    ![Example 2](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)

    ```
    Input: root = [1,0,1,0,0,0,1]
    Output: [1,null,1,null,1]
    ```

    ![Example 3](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)

    ```
    Input: root = [1,1,0,1,1,0,1,0]
    Output: [1,1,0,1,1,null,1]
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 200]
    - Node.val is either 0 or 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def prune_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
            raise NotImplementedError('Implement prune_tree')

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
