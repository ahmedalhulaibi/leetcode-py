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
    # 662. Maximum Width of Binary Tree

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a binary tree, return *the **maximum width** of the given tree*.

    The **maximum width** of a tree is the maximum **width** among all levels.

    The **width** of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

    It is **guaranteed** that the answer will in the range of a **32-bit** signed integer.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg)

    ```
    Input: root = [1,3,2,5,3,null,9]
    Output: 4
    Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/03/14/maximum-width-of-binary-tree-v3.jpg)

    ```
    Input: root = [1,3,2,5,null,null,9,6,null,7]
    Output: 7
    Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg)

    ```
    Input: root = [1,3,2,5]
    Output: 2
    Explanation: The maximum width exists in the second level with length 2 (3,2).
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 3000]`.
    - `-100 <= Node.val <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def width_of_binary_tree(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement width_of_binary_tree')

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
