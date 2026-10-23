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
    # 2009. Minimum Number of Operations to Make Array Continuous

    **Hard** · Array, Hash Table, Binary Search, Sliding Window

    You are given an integer array `nums`. In one operation, you can replace **any** element in `nums` with **any** integer.

    `nums` is considered **continuous** if both of the following conditions are fulfilled:

    - All elements in `nums` are **unique**.
    - The difference between the **maximum** element and the **minimum** element in `nums` equals `nums.length - 1`.

    For example, `nums = [4, 2, 5, 3]` is **continuous**, but `nums = [1, 2, 3, 5, 6]` is **not continuous**.

    Return *the **minimum** number of operations to make* `nums` *continuous*.

    ## Examples

    ```
    Input: nums = [4,2,5,3]
    Output: 0
    Explanation: nums is already continuous.
    ```

    ```
    Input: nums = [1,2,3,5,6]
    Output: 1
    Explanation: One possible solution is to change the last element to 4.
    The resulting array is [1,2,3,5,4], which is continuous.
    ```

    ```
    Input: nums = [1,10,100,1000]
    Output: 3
    Explanation: One possible solution is to change the last three elements to 2, 3 and 4.
    The resulting array is [1,2,3,4], which is continuous.
    ```

    ## Constraints

    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_operations(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement min_operations')

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
