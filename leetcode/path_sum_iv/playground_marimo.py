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
    # 666. Path Sum IV

    **Medium** · Array, Hash Table, Tree, Depth-First Search, Binary Tree

    If the depth of a tree is smaller than `5`, then this tree can be represented by an array of three-digit integers. You are given an **ascending** array `nums` consisting of three-digit integers representing a binary tree with a depth smaller than `5`, where for each integer:

    - The hundreds digit represents the depth `d` of this node, where `1 <= d <= 4`.
    - The tens digit represents the position `p` of this node within its level, where `1 <= p <= 8`, corresponding to its position in a **full binary tree**.
    - The units digit represents the value `v` of this node, where `0 <= v <= 9`.

    Return the **sum** of all **paths** from the **root** towards the **leaves**.

    It is **guaranteed** that the given array represents a valid connected binary tree.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0666.Path%20Sum%20IV/images/pathsum4-1-tree.jpg)

    ```
    Input: nums = [113,215,221]
    Output: 12
    Explanation: The tree that the list represents is shown. The path sum is (3 + 5) + (3 + 1) = 12.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0666.Path%20Sum%20IV/images/pathsum4-2-tree.jpg)

    ```
    Input: nums = [113,221]
    Output: 4
    Explanation: The tree that the list represents is shown. The path sum is (3 + 1) = 4.
    ```

    ## Constraints

    - 1 <= nums.length <= 15
    - 110 <= nums[i] <= 489
    - nums represents a valid binary tree with depth less than 5.
    - nums is sorted in ascending order.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def path_sum(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement path_sum')

    practice_exports = {'Solution': Solution}
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
