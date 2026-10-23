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
    # 333. Largest BST Subtree

    **Medium** · Tree, Depth-First Search, Binary Search Tree, Dynamic Programming, Binary Tree

    Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

    A **Binary Search Tree (BST)** is a tree in which all the nodes follow the below-mentioned properties:

    - The left subtree values are less than the value of their parent (root) node's value.
    - The right subtree values are greater than the value of their parent (root) node's value.

    **Note:** A subtree must include all of its descendants.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0333.Largest%20BST%20Subtree/images/tmp.jpg)

    ```
    Input: root = [10,5,15,1,8,null,7]
    Output: 3
    Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.
    ```

    ```
    Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
    Output: 2
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `-10^4 <= Node.val <= 10^4`

    **Follow up:** Can you figure out ways to solve it with `O(n)` time complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def largest_bst_subtree(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement largest_bst_subtree')

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
