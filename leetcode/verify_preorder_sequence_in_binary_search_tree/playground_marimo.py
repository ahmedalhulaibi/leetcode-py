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
    # 255. Verify Preorder Sequence in Binary Search Tree

    **Medium** · Stack, Tree, Binary Search Tree, Recursion, Array, Binary Tree, Monotonic Stack

    Given an array of **unique** integers `preorder`, return `true` *if it is the correct preorder traversal sequence of a binary search tree*.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0255.Verify%20Preorder%20Sequence%20in%20Binary%20Search%20Tree/images/preorder-tree.jpg)

    ```
    Input: preorder = [5,2,1,3,6]
    Output: true
    ```

    ```
    Input: preorder = [5,2,6,1,3]
    Output: false
    ```

    ## Constraints

    - `1 <= preorder.length <= 10^4`
    - `1 <= preorder[i] <= 10^4`
    - All the elements of `preorder` are **unique**.

    **Follow up:** Could you do it using only constant space complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def verify_preorder(self, preorder: list[int]) -> bool:
            raise NotImplementedError('Implement verify_preorder')

    practice_exports = {'Solution': Solution}
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
