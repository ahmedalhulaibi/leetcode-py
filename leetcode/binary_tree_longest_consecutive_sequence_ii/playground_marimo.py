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
    # 549. Binary Tree Longest Consecutive Sequence II

    **Medium** · Tree, Depth-First Search, Binary Tree, Tree DP

    Given the `root` of a binary tree, return the length of the longest consecutive path in the tree.

    A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.

    - For example, `[1,2,3,4]` and `[4,3,2,1]` are both considered valid, but the path `[1,2,4,3]` is not valid.

    On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0549.Binary%20Tree%20Longest%20Consecutive%20Sequence%20II/images/consec2-1-tree.jpg)

    ```
    Input: root = [1,2,3]
    Output: 2
    Explanation: The longest consecutive path is [1, 2] or [2, 1].
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0549.Binary%20Tree%20Longest%20Consecutive%20Sequence%20II/images/consec2-2-tree.jpg)

    ```
    Input: root = [2,1,3]
    Output: 3
    Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
    - `-3 * 10^4 <= Node.val <= 3 * 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def longest_consecutive(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement longest_consecutive')

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
