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
    # 1214. Two Sum BSTs

    **Medium** · Stack, Tree, Depth-First Search, Binary Search Tree, Two Pointers, Binary Search, Binary Tree

    <p>Given the roots of two binary search trees, <code>root1</code> and <code>root2</code>, return <code>true</code> if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer <code>target</code>.</p>

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1214.Two%20Sum%20BSTs/images/ex1.png)

    ```
    Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
    Output: true
    Explanation: 2 and 3 sum up to 5.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1214.Two%20Sum%20BSTs/images/ex2.png)

    ```
    Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
    Output: false
    ```

    ## Constraints

    - The number of nodes in each tree is in the range [1, 5000].
    - -10^9 <= Node.val, target <= 10^9.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def two_sum_bsts(self, root1: TreeNode[int] | None, root2: TreeNode[int] | None, target: int) -> bool:
            raise NotImplementedError('Implement two_sum_bsts')

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
