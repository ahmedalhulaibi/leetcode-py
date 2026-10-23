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
    # 298. Binary Tree Longest Consecutive Sequence

    **Medium** · Tree, Depth-First Search, Binary Tree

    Given the `root` of a binary tree, return *the length of the longest **consecutive sequence path***.

    A **consecutive sequence path** is a path where the values **increase by one** along the path.

    Note that the path can start **at any node** in the tree, and you cannot go from a node to its parent in the path.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0298.Binary%20Tree%20Longest%20Consecutive%20Sequence/images/consec1-1-tree.jpg)

    ```
    Input: root = [1,null,3,2,4,null,null,null,5]
    Output: 3
    Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0298.Binary%20Tree%20Longest%20Consecutive%20Sequence/images/consec1-2-tree.jpg)

    ```
    Input: root = [2,null,3,2,null,1]
    Output: 2
    Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
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
