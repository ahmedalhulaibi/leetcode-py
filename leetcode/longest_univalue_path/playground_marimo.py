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
    # 687. Longest Univalue Path

    **Medium** · Tree, Depth-First Search, Binary Tree, Dynamic Programming

    Given the `root` of a binary tree, return *the length of the longest path, where each node in the path has the same value*. This path may or may not pass through the `root`.

    The **length** of the path between two nodes is represented by the number of edges between them.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg)

    ```
    Input: root = [5,4,5,1,1,null,5]
    Output: 2
    ```
    **Explanation:** The shown image shows that the longest path of the same value (i.e. 5).

    ![Example 2](https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg)

    ```
    Input: root = [1,4,5,4,4,null,5]
    Output: 2
    ```
    **Explanation:** The shown image shows that the longest path of the same value (i.e. 4).

    ## Constraints

    - The number of nodes in the tree is in the range [0, 10^4].
    - -1000 <= Node.val <= 1000
    - The depth of the tree will not exceed 1000.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def longest_univalue_path(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement longest_univalue_path')

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
