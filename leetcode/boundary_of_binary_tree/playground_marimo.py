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
    # 545. Boundary of Binary Tree

    **Medium** · Tree, Depth-First Search, Binary Tree

    The **boundary** of a binary tree is the concatenation of the **root**, the **left boundary**, the **leaves** ordered from left-to-right, and the **reverse order** of the **right boundary**.

    The **left boundary** is the set of nodes defined by the following:

    - The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is **empty**.
    - If a node is in the left boundary and has a left child, then the left child is in the left boundary.
    - If a node is in the left boundary, has **no** left child, but has a right child, then the right child is in the left boundary.
    - The leftmost leaf is **not** in the left boundary.

    The **right boundary** is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is **not** part of the **right boundary**, and the **right boundary** is empty if the root does not have a right child.

    The **leaves** are nodes that do not have any children. For this problem, the root is **not** a leaf.

    Given the `root` of a binary tree, return the values of its **boundary**.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0545.Boundary%20of%20Binary%20Tree/images/boundary1.jpg)

    ```
    Input: root = [1,null,2,3,4]
    Output: [1,3,4,2]
    Explanation:
    - The left boundary is empty because the root does not have a left child.
    - The right boundary follows the path starting from the root's right child 2 -> 4. 4 is a leaf, so the right boundary is [2].
    - The leaves from left to right are [3,4].
    Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0545.Boundary%20of%20Binary%20Tree/images/boundary2.jpg)

    ```
    Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
    Output: [1,2,4,7,8,9,10,6,3]
    Explanation:
    - The left boundary follows the path starting from the root's left child 2 -> 4. 4 is a leaf, so the left boundary is [2].
    - The right boundary follows the path down the rightmost path 3 -> 6 -> 10. 10 is a leaf, so the right boundary is [3,6].
    - The leaves from left to right are [4,7,8,9,10].
    Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-1000 <= Node.val <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def boundary_of_binary_tree(self, root: TreeNode[int] | None) -> list[int]:
            raise NotImplementedError('Implement boundary_of_binary_tree')

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
