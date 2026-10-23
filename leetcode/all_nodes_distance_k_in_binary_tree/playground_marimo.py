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
    # 863. All Nodes Distance K in Binary Tree

    **Medium** · Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

    The value of `target` is given as an integer (all node values are unique). You can return the answer in any order.

    ## Examples

    ![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

    ```
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
    Output: [7,4,1]
    Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
    ```

    ```
    Input: root = [1], target = 1, k = 3
    Output: []
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 500].
    - 0 <= Node.val <= 500
    - All the values `Node.val` are **unique**.
    - `target` is the value of one of the nodes in the tree.
    - 0 <= k <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque
    from leetcode_py import TreeNode

    class Solution:

        def distance_k(self, root: TreeNode[int] | None, target: int, k: int) -> list[int]:
            raise NotImplementedError('Implement distance_k')

    practice_exports = {'deque': deque, 'TreeNode': TreeNode, 'Solution': Solution}
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
