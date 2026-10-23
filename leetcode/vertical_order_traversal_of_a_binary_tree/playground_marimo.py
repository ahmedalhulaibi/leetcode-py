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
    # 987. Vertical Order Traversal of a Binary Tree

    **Hard** · Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree

    Given the `root` of a binary tree, calculate the vertical order traversal of the binary tree.

    For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.

    The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

    Return the vertical order traversal of the binary tree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/01/29/vtree1.jpg)

    ```
    Input: root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]
    ```

    Column -1: Only node 9 is in this column. Column 0: Nodes 3 and 15 are in this column in that order from top to bottom. Column 1: Only node 20 is in this column. Column 2: Only node 7 is in this column.

    ![Example 2](https://assets.leetcode.com/uploads/2021/01/29/vtree2.jpg)

    ```
    Input: root = [1,2,3,4,5,6,7]
    Output: [[4],[2],[1,5,6],[3],[7]]
    ```

    Column -2: Only node 4 is in this column. Column -1: Only node 2 is in this column. Column 0: Nodes 1, 5, and 6 are in this column. 1 is at the top, so it comes first. 5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6. Column 1: Only node 3 is in this column. Column 2: Only node 7 is in this column.

    ![Example 3](https://assets.leetcode.com/uploads/2021/01/29/vtree3.jpg)

    ```
    Input: root = [1,2,3,4,6,5,7]
    Output: [[4],[2],[1,5,6],[3],[7]]
    ```

    This case is the exact same as example 2, but with nodes 5 and 6 swapped. Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.

    ## Constraints

    - The number of nodes in the tree is in the range [1, 1000]
    - 0 <= Node.val <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def vertical_traversal(self, root: TreeNode[int] | None) -> list[list[int]]:
            raise NotImplementedError('Implement vertical_traversal')

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
