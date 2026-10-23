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
    # 536. Construct Binary Tree from String

    **Medium** · Stack, Tree, Depth-First Search, String, Binary Tree

    You need to construct a binary tree from a string consisting of parenthesis and integers.

    The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

    You always start to construct the **left** child node of the parent first if it exists.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0536.Construct%20Binary%20Tree%20from%20String/images/butree.jpg)

    ```
    Input: s = "4(2(3)(1))(6(5))"
    Output: [4,2,6,3,1,5]
    ```

    ```
    Input: s = "4(2(3)(1))(6(5)(7))"
    Output: [4,2,6,3,1,5,7]
    ```

    ```
    Input: s = "-4(2(3)(1))(6(5)(7))"
    Output: [-4,2,6,3,1,5,7]
    ```

    ## Constraints

    - 0 <= s.length <= 3 * 10^4
    - s consists of digits, '(', ')', and '-' only.
    - All numbers in the tree have value at most than 2^30.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def str2tree(self, s: str) -> TreeNode[int] | None:
            raise NotImplementedError('Implement str2tree')

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
