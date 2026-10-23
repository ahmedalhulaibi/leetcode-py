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
    # 2471. Minimum Number of Operations to Sort a Binary Tree by Level

    **Medium** · Tree, Breadth-First Search, Binary Tree

    You are given the `root` of a binary tree with **unique values**.

    In one operation, you can choose any two nodes **at the same level** and swap their values.

    Return the minimum number of operations needed to make the values at each level sorted in a **strictly increasing order**.

    The **level** of a node is the number of edges along the path between it and the root node.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/09/18/image-20220918174006-2.png)

    ```
    Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
    Output: 3
    Explanation:
    - Swap 4 and 3. The 2nd level becomes [3,4].
    - Swap 7 and 5. The 3rd level becomes [5,6,8,7].
    - Swap 8 and 7. The 3rd level becomes [5,6,7,8].
    We used 3 operations so return 3.
    It can be proven that 3 is the minimum number of operations needed.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/09/18/image-20220918174026-3.png)

    ```
    Input: root = [1,3,2,7,6,5,4]
    Output: 3
    Explanation:
    - Swap 3 and 2. The 2nd level becomes [2,3].
    - Swap 7 and 4. The 3rd level becomes [4,6,5,7].
    - Swap 6 and 5. The 3rd level becomes [4,5,6,7].
    We used 3 operations so return 3.
    It can be proven that 3 is the minimum number of operations needed.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2022/09/18/image-20220918174052-4.png)

    ```
    Input: root = [1,2,3,4,5,6]
    Output: 0
    Explanation: Each level is already sorted in increasing order so return 0.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 10^5]
    - 1 <= Node.val <= 10^5
    - All the values of the tree are unique



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def minimum_operations(self, root: TreeNode[int] | None) -> int:
            raise NotImplementedError('Implement minimum_operations')

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
