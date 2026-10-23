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
    # 865. Smallest Subtree with all the Deepest Nodes

    **Medium** · Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree, Binary Lifting, Lowest Common Ancestor, DP on Trees

    Given the `root` of a binary tree, the depth of each node is **the shortest distance to the root**.

    Return *the smallest subtree* such that it contains **all the deepest nodes** in the original tree.

    A node is called **the deepest** if it has the largest depth possible among any node in the entire tree.

    The **subtree** of a node is a tree consisting of that node, plus the set of all descendants of that node.

    ## Examples

    ![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png)

    ```
    Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation: We return the node with value 2, colored in yellow in the diagram.
    The nodes coloured in blue are the deepest nodes of the tree.
    Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is
    the smallest subtree among them, so we return it.
    ```

    ```
    Input: root = [1]
    Output: [1]
    Explanation: The root is the deepest node in the tree.
    ```

    ```
    Input: root = [0,1,3,null,2]
    Output: [2]
    Explanation: The deepest node in the tree is 2, the valid subtrees are the
    subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
    ```

    ## Constraints

    - The number of nodes in the tree will be in the range [1, 500].
    - 0 <= Node.val <= 500
    - The values of the nodes in the tree are unique.

    **Note:** This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def subtree_with_all_deepest(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
            raise NotImplementedError('Implement subtree_with_all_deepest')

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
