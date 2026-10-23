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
    # 1448. Count Good Nodes in Binary Tree

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given a binary tree `root`, a node *X* in the tree is named **good** if in the path from root to *X* there are no nodes with a value *greater than* X.

    Return the number of **good** nodes in the binary tree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png)

    ```
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path.
    Node 3 -> (3,1,3) is the maximum value in the path.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png)

    ```
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3,3,2) is not good, because "3" is higher than it.
    ```

    ```
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.
    ```

    ## Constraints

    - The number of nodes in the binary tree is in the range `[1, 10^5]`.
    - Each node's value is between `[-10^4, 10^4]`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def good_nodes(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement good_nodes')

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
