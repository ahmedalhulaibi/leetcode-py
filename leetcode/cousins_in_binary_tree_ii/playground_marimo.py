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
    # 2641. Cousins in Binary Tree II

    **Medium** · Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given the `root` of a binary tree, replace the value of each node in the tree with the **sum of all its cousins' values**.

    Two nodes of a binary tree are **cousins** if they have the same depth with different parents.

    Return the root of the modified tree.

    Note that the depth of a node is the number of edges in the path from the root node to it.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/01/11/example11.png)

    ```
    Input: root = [5,4,9,1,10,null,7]
    Output: [0,0,0,7,7,null,11]
    ```
    **Explanation:** Node with value 5 does not have any cousins so its sum is 0. Node with value 4 does not have any cousins so its sum is 0. Node with value 9 does not have any cousins so its sum is 0. Node with value 1 has a cousin with value 7 so its sum is 7. Node with value 10 has a cousin with value 7 so its sum is 7. Node with value 7 has cousins with values 1 and 10 so its sum is 11.

    ![Example 2](https://assets.leetcode.com/uploads/2023/01/11/diagram33.png)

    ```
    Input: root = [3,1,2]
    Output: [0,0,0]
    ```
    **Explanation:** Node with value 3 does not have any cousins so its sum is 0. Node with value 1 does not have any cousins so its sum is 0. Node with value 2 does not have any cousins so its sum is 0.

    ## Constraints

    - The number of nodes in the tree is in the range [1, 10^5].
    - 1 <= Node.val <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def replace_value_in_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
            raise NotImplementedError('Implement replace_value_in_tree')

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
