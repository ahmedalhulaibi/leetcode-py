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
    # 1120. Maximum Average Subtree

    **Medium** · Tree, Depth-First Search, Binary Tree

    Given the `root` of a binary tree, return *the maximum **average** value of a subtree of that tree*. Answers within `10^-5` of the actual answer will be accepted.

    A **subtree** of a tree is any node of that tree plus all its descendants.

    The **average** value of a tree is the sum of its values, divided by the number of nodes.

    ## Examples

    ```
    Input: root = [5,6,1]
    Output: 6.00000
    Explanation: For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4. For the node with value = 6 we have an average of 6 / 1 = 6. So the answer is 6 which is the maximum.
    ```

    ```
    Input: root = [0,null,1]
    Output: 1.00000
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 10^4].
    - 0 <= Node.val <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def maximum_average_subtree(self, root: TreeNode[int] | None) -> float:
            raise NotImplementedError('Implement maximum_average_subtree')

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
