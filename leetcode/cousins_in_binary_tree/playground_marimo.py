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
    # 993. Cousins in Binary Tree

    **Easy** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a binary tree with unique values and the values of two different nodes of the tree `x` and `y`, return `true` if the nodes corresponding to the values `x` and `y` in the tree are cousins, or `false` otherwise.

    Two nodes of a binary tree are **cousins** if they have the same depth with different parents.

    Note that in a binary tree, the root node is at the depth `0`, and children of each depth `k` node are at the depth `k + 1`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png)

    ```
    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)

    ```
    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png)

    ```
    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [2, 100]
    - 1 <= Node.val <= 100
    - Each node has a unique value
    - x != y
    - x and y exist in the tree



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def is_cousins(self, root: TreeNode[int] | None, x: int, y: int) -> bool:
            raise NotImplementedError('Implement is_cousins')

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
