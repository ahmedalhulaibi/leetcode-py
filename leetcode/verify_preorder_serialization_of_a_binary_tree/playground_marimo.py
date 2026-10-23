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
    # 331. Verify Preorder Serialization of a Binary Tree

    **Medium** · String, Stack, Tree, Binary Tree

    One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as `#`.

    For example, the above binary tree can be serialized to the string `"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where `'#'` represents a null node.

    Given a string of comma-separated values `preorder`, return `true` if it is a correct preorder traversal serialization of a binary tree.

    It is **guaranteed** that each comma-separated value in the string must be either an integer or a character `'#'` representing null pointer.

    You may assume that the input format is always valid.

    - For example, it could never contain two consecutive commas, such as `"1,,3"`.

    **Note:** You are not allowed to reconstruct the tree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/12/pre-tree.jpg)

    ```
    Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    Output: true
    ```

    ```
    Input: preorder = "1,#"
    Output: false
    ```

    ```
    Input: preorder = "9,#,#,1"
    Output: false
    ```

    ## Constraints

    - 1 <= preorder.length <= 10^4
    - preorder consist of integers in the range [0, 100] and '#' separated by commas ','.

    **Note:** You are not allowed to reconstruct the tree.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_valid_serialization(self, preorder: str) -> bool:
            raise NotImplementedError('Implement is_valid_serialization')

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
