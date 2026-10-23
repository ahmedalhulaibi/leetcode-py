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
    # 938. Range Sum of BST

    **Easy** · Tree, Depth-First Search, Binary Search Tree, Binary Tree

    <p>Given the <code>root</code> node of a binary search tree and two integers <code>low</code> and <code>high</code>, return <em>the sum of values of all nodes with a value in the <strong>inclusive</strong> range </em><code>[low, high]</code>.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg)

    ```
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg)

    ```
    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
    Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
    ```

    ## Constraints

    <ul>
        <li>The number of nodes in the tree is in the range <code>[1, 2 * 10^4]</code>.</li>
        <li><code>1 &lt;= Node.val &lt;= 10^5</code></li>
        <li><code>1 &lt;= low &lt;= high &lt;= 10^5</code></li>
        <li>All <code>Node.val</code> are <strong>unique</strong>.</li>
    </ul>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def range_sum_bst(self, root: TreeNode[int] | None, low: int, high: int) -> int:
            raise NotImplementedError('Implement range_sum_bst')

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
