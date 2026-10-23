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
    # 272. Closest Binary Search Tree Value II

    **Hard** · Stack, Tree, Depth-First Search, Binary Search Tree, Two Pointers, Binary Tree, Heap (Priority Queue)

    Given the `root` of a binary search tree, a `target` value, and an integer `k`, return *the* `k` *values in the BST that are closest to the* `target`. You may return the answer in **any order**.

    You are **guaranteed** to have only one unique set of `k` values in the BST that are closest to the `target`.

    **Follow up:** Assume that the BST is balanced. Could you solve it in less than `O(n)` runtime (where `n = total nodes`)?

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0272.Closest%20Binary%20Search%20Tree%20Value%20II/images/closest1-1-tree.jpg)

    ```
    Input: root = [4,2,5,1,3], target = 3.714286, k = 2
    Output: [4,3]
    ```

    ```
    Input: root = [1], target = 0.000000, k = 1
    Output: [1]
    ```

    ## Constraints

    - The number of nodes in the tree is `n`.
    - `1 <= k <= n <= 10^4`.
    - `0 <= Node.val <= 10^9`
    - `-10^9 <= target <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import heapq
    from leetcode_py import TreeNode

    class Solution:

        def closest_k_values(self, root: TreeNode[int], target: float, k: int) -> list[int]:
            raise NotImplementedError('Implement closest_k_values')

    practice_exports = {'heapq': heapq, 'TreeNode': TreeNode, 'Solution': Solution}
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
