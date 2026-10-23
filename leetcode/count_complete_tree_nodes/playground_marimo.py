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
    # 222. Count Complete Tree Nodes

    **Medium** · Binary Search, Bit Manipulation, Tree, Binary Tree

    Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.

    According to Wikipedia's definition of a complete binary tree, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `1` and `2^h` nodes inclusive at the last level `h`.

    Design an algorithm that runs in less than `O(n)` time complexity.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)

    ```
    Input: root = [1,2,3,4,5,6]
    Output: 6
    ```

    ```
    Input: root = []
    Output: 0
    ```

    ```
    Input: root = [1]
    Output: 1
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 5 * 10^4]`.
    - `0 <= Node.val <= 5 * 10^4`
    - The tree is guaranteed to be **complete**.

    **Follow up:** Design an algorithm that runs in less than `O(n)` time complexity.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def count_nodes(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement count_nodes')

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
