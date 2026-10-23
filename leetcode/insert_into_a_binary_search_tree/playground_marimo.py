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
    # 701. Insert into a Binary Search Tree

    **Medium** · Tree, Binary Search Tree, Binary Tree

    You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return _the root node of the BST after the insertion_. It is **guaranteed** that the new value does not exist in the original BST.

    **Notice** that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return **any of them**.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)

    ```
    Input: root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5]
    Explanation: Another accepted tree is:

    ![Example 1 alt](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)
    ```

    ```
    Input: root = [40,20,60,10,30,50,70], val = 25
    Output: [40,20,60,10,30,50,70,null,null,25]
    ```

    ```
    Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
    Output: [4,2,7,1,3,5]
    ```

    ## Constraints

    - The number of nodes in the tree will be in the range [0, 10^4].
    - -10^8 <= Node.val <= 10^8
    - All the values `Node.val` are **unique**.
    - -10^8 <= val <= 10^8
    - It's **guaranteed** that `val` does not exist in the original BST.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def insert_into_bst(self, root: TreeNode[int] | None, val: int) -> TreeNode[int] | None:
            raise NotImplementedError('Implement insert_into_bst')

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
