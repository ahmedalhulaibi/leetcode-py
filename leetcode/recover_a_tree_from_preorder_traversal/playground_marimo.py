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
    # 1028. Recover a Tree From Preorder Traversal

    **Hard** · String, Tree, Depth-First Search, Binary Tree

    We run a preorder depth-first search (DFS) on the `root` of a binary tree.

    At each node in this traversal, we output `D` dashes (where `D` is the depth of this node), then we output the value of this node. If the depth of a node is `D`, the depth of its immediate child is `D + 1`. The depth of the `root` node is `0`.

    If a node has only one child, that child is guaranteed to be **the left child**.

    Given the output traversal of this traversal, recover the tree and return its `root`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/09/10/recover_tree_ex1.png)

    ```
    Input: traversal = "1-2--3--4-5--6--7"
    Output: [1,2,5,3,4,6,7]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2024/09/10/recover_tree_ex2.png)

    ```
    Input: traversal = "1-2--3---4-5--6---7"
    Output: [1,2,5,3,null,6,null,4,null,7]
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2024/09/10/recover_tree_ex3.png)

    ```
    Input: traversal = "1-401--349---90--88"
    Output: [1,401,null,349,88,90]
    ```

    ## Constraints

    - The number of nodes in the original tree is in the range `[1, 1000]`.
    - `1 <= Node.val <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def recover_from_preorder(self, traversal: str) -> TreeNode[int] | None:
            raise NotImplementedError('Implement recover_from_preorder')

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
