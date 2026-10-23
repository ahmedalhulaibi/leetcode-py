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
    # 1609. Even Odd Tree

    **Medium** · Tree, Breadth-First Search, Binary Tree

    A binary tree is named Even-Odd if it meets the following conditions:

    - The root of the binary tree is at level index `0`, its children are at level index `1`, their children are at level index `2`, etc.
    - For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
    - For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

    Given the `root` of a binary tree, return `true` if the binary tree is Even-Odd, otherwise return `false`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/15/sample_1_1966.png)

    ```
    Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
    Output: true
    Explanation: The node values on each level are:
    Level 0: [1]
    Level 1: [10,4]
    Level 2: [3,7,9]
    Level 3: [12,8,6,2]
    Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/09/15/sample_2_1966.png)

    ```
    Input: root = [5,4,2,3,3,7]
    Output: false
    Explanation: The node values on each level are:
    Level 0: [5]
    Level 1: [4,2]
    Level 2: [3,3,7]
    Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2020/09/22/sample_1_333_1966.png)

    ```
    Input: root = [5,9,1,3,5,7]
    Output: false
    Explanation: Node values in the level 1 should be even integers.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 10^5].
    - 1 <= Node.val <= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def is_even_odd_tree(self, root: TreeNode[int] | None) -> bool:
            raise NotImplementedError('Implement is_even_odd_tree')

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
