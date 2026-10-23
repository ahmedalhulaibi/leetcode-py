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
    # 1530. Number of Good Leaf Nodes Pairs

    **Medium** · Tree, Depth-First Search, Binary Tree, DP on Trees

    You are given the `root` of a binary tree and an integer `distance`.

    A pair of two different **leaf** nodes of a binary tree is said to be good if the length of **the shortest path** between them is less than or equal to `distance`.

    Return *the number of good leaf node pairs* in the tree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/07/09/e1.jpg)

    ```
    Input: root = [1,2,3,null,4], distance = 3
    Output: 1
    ```
    **Explanation:** The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

    ![Example 2](https://assets.leetcode.com/uploads/2020/07/09/e2.jpg)

    ```
    Input: root = [1,2,3,4,5,6,7], distance = 3
    Output: 2
    ```
    **Explanation:** The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of the shortest path between them is 4.

    ```
    Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
    Output: 1
    ```
    **Explanation:** The only good pair is [2,5].

    ## Constraints

    - The number of nodes in the tree is in the range [1, 2^10].
    - 1 <= Node.val <= 100
    - 1 <= distance <= 10



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def count_pairs(self, root: TreeNode[int] | None, distance: int) -> int:
            raise NotImplementedError('Implement count_pairs')

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
