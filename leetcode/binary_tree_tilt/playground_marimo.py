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
    # 563. Binary Tree Tilt

    **Easy** · Tree, Depth-First Search, Binary Tree, DP on Trees

    Given the `root` of a binary tree, return *the sum of every tree node's **tilt***.

    The **tilt** of a tree node is the **absolute difference** between the sum of all left subtree node **values** and all right subtree node **values**. If a node does not have a left child, then the sum of the left subtree node **values** is treated as `0`. The rule is similar if the node does not have a right child.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/20/tilt1.jpg)

    ```
    Input: root = [1,2,3]
    Output: 1
    Explanation:
    Tilt of node 2 : |0-0| = 0 (no children)
    Tilt of node 3 : |0-0| = 0 (no children)
    Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
    Sum of every tilt : 0 + 0 + 1 = 1
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/10/20/tilt2.jpg)

    ```
    Input: root = [4,2,9,3,5,null,7]
    Output: 15
    Explanation:
    Tilt of node 3 : |0-0| = 0 (no children)
    Tilt of node 5 : |0-0| = 0 (no children)
    Tilt of node 7 : |0-0| = 0 (no children)
    Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
    Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
    Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
    Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2020/10/20/tilt3.jpg)

    ```
    Input: root = [21,7,14,1,1,2,2,3,3]
    Output: 9
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `-1000 <= Node.val <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def find_tilt(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement find_tilt')

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
