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
    # 742. Closest Leaf in a Binary Tree

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a binary tree where every node has a **unique value** and a target integer `k`, return *the value of the nearest leaf node to the target* `k` *in the tree*.

    Nearest to a leaf means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

    In case of a tie, any leaf with the minimum distance is accepted.

    ## Examples

    ```
    Input: root = [1,3,2], k = 1
    Output: 2
    Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
    ```

    ```
    Input: root = [1], k = 1
    Output: 1
    Explanation: The nearest leaf node is the root node itself.
    ```

    ```
    Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
    Output: 3
    Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 1000].
    - 1 <= Node.val <= 1000
    - All the values of the tree are unique.
    - There exist some node in the tree where Node.val == k.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def find_closest_leaf(self, root: TreeNode[int] | None, k: int) -> int:
            raise NotImplementedError('Implement find_closest_leaf')

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
