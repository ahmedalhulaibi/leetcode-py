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
    # 654. Maximum Binary Tree

    **Medium** · Array, Divide and Conquer, Stack, Tree, Monotonic Stack, Binary Tree

    You are given an integer array `nums` with no duplicates. A **maximum binary tree** can be built recursively from `nums` using the following algorithm:

    1. Create a root node whose value is the maximum value in `nums`.
    2. Recursively build the left subtree on the **subarray prefix** to the **left** of the maximum value.
    3. Recursively build the right subtree on the **subarray suffix** to the **right** of the maximum value.

    Return the maximum binary tree built from `nums`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg)

    ```
    Input: nums = [3,2,1,6,0,5]
    Output: [6,3,5,null,2,0,null,null,1]
    Explanation: The recursive calls are as follow:
    - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
        - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
            - Empty array, so no child.
            - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
                - Empty array, so no child.
                - Only one element, so child is a node with value 1.
        - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
            - Only one element, so child is a node with value 0.
            - Empty array, so no child.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg)

    ```
    Input: nums = [3,2,1]
    Output: [3,null,2,null,1]
    ```

    ## Constraints

    - 1 <= nums.length <= 1000
    - 0 <= nums[i] <= 1000
    - All integers in nums are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def construct_maximum_binary_tree(self, nums: list[int]) -> TreeNode[int] | None:
            raise NotImplementedError('Implement construct_maximum_binary_tree')

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
