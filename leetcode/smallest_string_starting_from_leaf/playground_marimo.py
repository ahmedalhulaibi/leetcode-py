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
    # 988. Smallest String Starting From Leaf

    **Medium** · String, Backtracking, Tree, Depth-First Search, Binary Tree

    You are given the `root` of a binary tree where each node has a value in the range `[0, 25]` representing the letters `'a'` to `'z'`.

    Return *the lexicographically smallest string that starts at a leaf of this tree and ends at the root*.

    As a reminder, any shorter prefix of a string is lexicographically smaller.

    - For example, `"ab"` is lexicographically smaller than `"aba"`.

    A leaf of a node is a node that has no children.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/01/30/tree1.png)

    ```
    Input: root = [0,1,2,3,4,3,4]
    Output: "dba"
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/01/30/tree2.png)

    ```
    Input: root = [25,1,3,1,3,0,2]
    Output: "adz"
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2019/02/01/tree3.png)

    ```
    Input: root = [2,2,1,null,1,0,null,0]
    Output: "abc"
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 8500]`.
    - `0 <= Node.val <= 25`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def smallest_from_leaf(self, root: TreeNode[int] | None) -> str:
            raise NotImplementedError('Implement smallest_from_leaf')

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
