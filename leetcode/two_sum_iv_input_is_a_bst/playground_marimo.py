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
    mo.md(r"""
    # 653. Two Sum IV - Input is a BST

    **Easy** · Hash Table, Two Pointers, Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree

    <p>Given the <code>root</code> of a binary search tree and an integer <code>k</code>, return <code>true</code> <em>if there exist two elements in the BST such that their sum is equal to</em> <code>k</code>, <em>or</em> <code>false</code> <em>otherwise</em>.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)

    ```
    Input: root = [5,3,6,2,4,null,7], k = 9
    Output: true
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)

    ```
    Input: root = [5,3,6,2,4,null,7], k = 28
    Output: false
    ```

    ## Constraints

    <ul>
        <li>The number of nodes in the tree is in the range <code>[1, 10^4]</code>.</li>
        <li><code>-10^4 &lt;= Node.val &lt;= 10^4</code></li>
        <li><code>root</code> is guaranteed to be a <strong>valid</strong> binary search tree.</li>
        <li><code>-10^5 &lt;= k &lt;= 10^5</code></li>
    </ul>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def find_target(self, root: TreeNode[int] | None, k: int) -> bool:
            raise NotImplementedError('Implement find_target')

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
