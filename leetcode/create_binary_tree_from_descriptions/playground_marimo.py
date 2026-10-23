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
    # 2196. Create Binary Tree From Descriptions

    **Medium** · Array, Hash Table, Tree, Binary Tree

    You are given a 2D integer array `descriptions` where `descriptions[i] = [parent<sub>i</sub>, child<sub>i</sub>, isLeft<sub>i</sub>]` indicates that `parent<sub>i</sub>` is the **parent** of `child<sub>i</sub>` in a **binary** tree of **unique** values. Furthermore,

    - If `isLeft<sub>i</sub> == 1`, then `child<sub>i</sub>` is the left child of `parent<sub>i</sub>`.
    - If `isLeft<sub>i</sub> == 0`, then `child<sub>i</sub>` is the right child of `parent<sub>i</sub>`.

    Construct the binary tree described by `descriptions` and return its **root**.

    The test cases will be generated such that the binary tree is **valid**.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png)

    ```
    Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    Output: [50,20,80,15,17,19]
    Explanation: The root node is the node with value 50 since it has no parent.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png)

    ```
    Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
    Output: [1,2,null,null,3,4]
    Explanation: The root node is the node with value 1 since it has no parent.
    ```

    ## Constraints

    - 1 <= descriptions.length <= 10^4
    - descriptions[i].length == 3
    - 1 <= parent<sub>i</sub>, child<sub>i</sub> <= 10^5
    - 0 <= isLeft<sub>i</sub> <= 1
    - The binary tree described by descriptions is valid.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def create_binary_tree(self, descriptions: list[list[int]]) -> TreeNode[int] | None:
            raise NotImplementedError('Implement create_binary_tree')

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
