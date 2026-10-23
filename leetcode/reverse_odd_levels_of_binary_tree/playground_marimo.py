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
    # 2415. Reverse Odd Levels of Binary Tree

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a <strong>perfect</strong> binary tree, reverse the node values at each <strong>odd</strong> level of the tree.

    For example, suppose the node values at level 3 are `[2,1,3,4,7,11,29,18]`, then it should become `[18,29,11,7,4,3,1,2]`.

    Return <em>the root of the reversed tree</em>.

    A binary tree is <strong>perfect</strong> if all parent nodes have two children and all leaves are on the same level.

    The <strong>level</strong> of a node is the number of edges along the path between it and the root node.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/07/28/first_case1.png)

    ```
    Input: root = [2,3,5,8,13,21,34]
    Output: [2,5,3,8,13,21,34]
    Explanation:
    The tree has only one odd level.
    The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/07/28/second_case3.png)

    ```
    Input: root = [7,13,11]
    Output: [7,11,13]
    Explanation:
    The nodes at level 1 are 13, 11, which are reversed and become 11, 13.
    ```

    ```
    Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
    Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
    Explanation:
    The odd levels have non-zero values.
    The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
    The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 2^14]
    - 0 <= Node.val <= 10^5
    - root is a perfect binary tree



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def reverse_odd_levels(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
            raise NotImplementedError('Implement reverse_odd_levels')

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
