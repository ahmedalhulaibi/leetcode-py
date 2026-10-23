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
    # 894. All Possible Full Binary Trees

    **Medium** · Dynamic Programming, Tree, Recursion, Memoization, Binary Tree

    Given an integer <code>n</code>, return <em>a list of all possible <strong>full binary trees</strong> with</em> <code>n</code> <em>nodes</em>. Each node of each tree in the answer must have <code>Node.val == 0</code>.</p>

    <p>Each element of the answer is the root node of one possible tree. You may return the final list of trees in <strong>any order</strong>.</p>

    <p>A <strong>full binary tree</strong> is a binary tree where each node has exactly <code>0</code> or <code>2</code> children.</p>

    ## Examples

    ```
    Input: n = 7
    Output: [[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,0,0,None,None,0,0],[0,0,0,0,0,None,None,0,0],[0,0,0,0,0,0,0]]
    ```

    ```
    Input: n = 3
    Output: [[0,0,0]]
    ```

    ## Constraints

    - 1 <= n <= 20



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def all_possible_fbt(self, n: int) -> list[TreeNode[int] | None]:
            raise NotImplementedError('Implement all_possible_fbt')

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
