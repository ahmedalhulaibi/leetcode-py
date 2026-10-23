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
    # 314. Binary Tree Vertical Order Traversal

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree, Sorting

    Given the `root` of a binary tree, return **the vertical order traversal** of its nodes' values. (i.e., from top to bottom, column by column).

    If two nodes are in the same row and column, the order should be from **left to right**.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0314.Binary%20Tree%20Vertical%20Order%20Traversal/images/image1.png)

    ```
    Input: root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0314.Binary%20Tree%20Vertical%20Order%20Traversal/images/image3.png)

    ```
    Input: root = [3,9,8,4,0,1,7]
    Output: [[4],[9],[3,0,1],[8],[7]]
    ```

    ![Example 3](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0314.Binary%20Tree%20Vertical%20Order%20Traversal/images/image2.png)

    ```
    Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
    Output: [[4],[2,5],[1,10,9,6],[3],[11]]
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def vertical_order(self, root: TreeNode[int] | None) -> list[list[int]]:
            raise NotImplementedError('Implement vertical_order')

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
