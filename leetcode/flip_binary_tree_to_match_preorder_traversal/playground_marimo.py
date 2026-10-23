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
    # 971. Flip Binary Tree To Match Preorder Traversal

    **Medium** · Tree, Depth-First Search, Binary Tree

    You are given the `root` of a binary tree with `n` nodes, where each node is uniquely assigned a value from `1` to `n`. You are also given a sequence of `n` values `voyage`, which is the **desired** **pre-order traversal** of the binary tree.

    Any node in the binary tree can be **flipped** by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:

    ![Flip example](https://assets.leetcode.com/uploads/2021/02/15/fliptree.jpg)

    Flip the **smallest** number of nodes so that the **pre-order traversal** of the tree **matches** `voyage`.

    Return a list of the values of all **flipped** nodes. You may return the answer in **any order**. If it is **impossible** to flip the nodes in the tree to make the pre-order traversal match `voyage`, return the list `[-1]`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/01/02/1219-01.png)

    ```
    Input: root = [1,2], voyage = [2,1]
    Output: [-1]
    Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/01/02/1219-02.png)

    ```
    Input: root = [1,2,3], voyage = [1,3,2]
    Output: [1]
    Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2019/01/02/1219-02.png)

    ```
    Input: root = [1,2,3], voyage = [1,2,3]
    Output: []
    Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.
    ```

    ## Constraints

    - The number of nodes in the tree is n
    - n == voyage.length
    - 1 <= n <= 100
    - 1 <= Node.val, voyage[i] <= n
    - All the values in the tree are unique
    - All the values in voyage are unique



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def flip_match_voyage(self, root: TreeNode[int] | None, voyage: list[int]) -> list[int]:
            raise NotImplementedError('Implement flip_match_voyage')

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
