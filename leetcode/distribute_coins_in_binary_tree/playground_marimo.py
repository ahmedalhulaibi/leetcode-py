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
    # 979. Distribute Coins in Binary Tree

    **Medium** · Tree, Depth-First Search, Binary Tree, Dynamic Programming

    You are given the `root` of a binary tree with `n` nodes where each node in the tree has `node.val` coins. There are `n` coins in total throughout the whole tree.

    In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

    Return *the minimum number of moves required to make every node have exactly one* coin.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/01/18/tree1.png)

    ```
    Input: root = [3,0,0]
    Output: 2
    Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/01/18/tree2.png)

    ```
    Input: root = [0,3,0]
    Output: 3
    Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
    ```

    ## Constraints

    - The number of nodes in the tree is `n`.
    - `1 <= n <= 100`
    - `0 <= Node.val <= n`
    - The sum of all `Node.val` is `n`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def distribute_coins(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement distribute_coins')

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
