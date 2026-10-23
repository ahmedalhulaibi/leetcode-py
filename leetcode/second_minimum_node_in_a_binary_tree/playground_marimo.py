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
    # 671. Second Minimum Node In a Binary Tree

    **Easy** · Tree, Depth-First Search, Binary Tree

    Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly `two` or `zero` sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property `root.val = min(root.left.val, root.right.val)` always holds.

    Given such a binary tree, you need to output the **second minimum** value in the set made of all the nodes' value in the whole tree.

    If no such second minimum value exists, output -1 instead.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg)

    ```
    Input: root = [2,2,5,null,null,5,7]
    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg)

    ```
    Input: root = [2,2,2]
    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 25]
    - 1 <= Node.val <= 2^31 - 1
    - root.val == min(root.left.val, root.right.val) for each internal node of the tree



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def find_second_minimum_value(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement find_second_minimum_value')

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
