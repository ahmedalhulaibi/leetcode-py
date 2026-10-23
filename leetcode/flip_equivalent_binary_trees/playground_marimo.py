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
    mo.md(r"""
    # 951. Flip Equivalent Binary Trees

    **Medium** · Tree, Depth-First Search, Binary Tree

    <p>For a binary tree <strong>T</strong>, we can define a <strong>flip operation</strong> as follows: choose any node, and swap the left and right child subtrees.</p>

    <p>A binary tree <strong>X</strong>&nbsp;is <strong>flip equivalent</strong> to a binary tree <strong>Y</strong> if and only if we can make <strong>X</strong> equal to <strong>Y</strong> after some number of flip operations.</p>

    <p>Given the roots of two binary trees <code>root1</code> and <code>root2</code>, return <code>true</code> if the two trees are flip equivalent or <code>false</code> otherwise.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png)

    ```
    Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    Output: true
    Explanation: We flipped at nodes with values 1, 3, and 5.
    ```

    ```
    Input: root1 = [], root2 = []
    Output: true
    ```

    ```
    Input: root1 = [], root2 = [1]
    Output: false
    ```

    ## Constraints

    <ul>
        <li>The number of nodes in each tree is in the range <code>[0, 100]</code>.</li>
        <li>Each tree will have <strong>unique node values</strong> in the range <code>[0, 99]</code>.</li>
    </ul>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def flip_equiv(self, root1: TreeNode[int] | None, root2: TreeNode[int] | None) -> bool:
            raise NotImplementedError('Implement flip_equiv')

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
