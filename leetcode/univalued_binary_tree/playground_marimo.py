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
    # 965. Univalued Binary Tree

    **Easy** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    A binary tree is <strong>uni-valued</strong> if every node in the tree has the same value.

    Given the <code>root</code> of a binary tree, return <code>true</code> if the given tree is <strong>uni-valued</strong>, or <code>false</code> otherwise.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png)

    ```
    Input: root = [1,1,1,1,1,null,1]
    Output: true
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png)

    ```
    Input: root = [2,2,2,5,2]
    Output: false
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 100]
    - 0 <= Node.val < 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def is_unival_tree(self, root: TreeNode[int] | None) -> bool:
            raise NotImplementedError('Implement is_unival_tree')

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
