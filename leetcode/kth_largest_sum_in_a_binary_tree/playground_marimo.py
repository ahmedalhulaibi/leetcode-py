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
    # 2583. Kth Largest Sum in a Binary Tree

    **Medium** · Tree, Breadth-First Search, Sorting, Binary Tree

    You are given the `root` of a binary tree and a positive integer `k`.

    The **level sum** in the tree is the sum of the values of the nodes that are on the **same** level.

    Return *the* `kth` *largest level sum in the tree (not necessarily distinct)*. If there are fewer than `k` levels in the tree, return `-1`.

    Note that two nodes are on the same level if they have the same distance from the root.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/12/14/binaryytreeedrawio-2.png)

    ```
    Input: root = [5,8,9,2,1,3,7,4,6], k = 2
    Output: 13
    Explanation: The level sums are the following:
    - Level 1: 5.
    - Level 2: 8 + 9 = 17.
    - Level 3: 2 + 1 + 3 + 7 = 13.
    - Level 4: 4 + 6 = 10.
    The 2nd largest level sum is 13.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/12/14/treedrawio-3.png)

    ```
    Input: root = [1,2,null,3], k = 1
    Output: 3
    Explanation: The largest level sum is 3.
    ```

    ## Constraints

    - The number of nodes in the tree is `n`.
    - `2 <= n <= 10^5`
    - `1 <= Node.val <= 10^6`
    - `1 <= k <= n`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def kth_largest_level_sum(self, root: TreeNode[int] | None, k: int) -> int:
            raise NotImplementedError('Implement kth_largest_level_sum')

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
