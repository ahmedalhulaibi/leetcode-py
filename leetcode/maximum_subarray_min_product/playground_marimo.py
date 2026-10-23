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
    # 1856. Maximum Subarray Min-Product

    **Medium** · Array, Stack, Monotonic Stack, Prefix Sum, Cartesian Tree

    The **min-product** of an array is equal to the **minimum value** in the array **multiplied by** the array's **sum**.

    - For example, the array `[3,2,5]` (minimum value is `2`) has a min-product of `2 * (3+2+5) = 2 * 10 = 20`.

    Given an array of integers `nums`, return *the **maximum min-product** of any **non-empty subarray** of* `nums`. Since the answer may be large, return it **modulo** `10^9 + 7`.

    Note that the min-product should be maximized **before** performing the modulo operation. Testcases are generated such that the maximum min-product **without** modulo will fit in a **64-bit signed integer**.

    A **subarray** is a **contiguous** part of an array.

    ## Examples

    ```
    Input: nums = [1,2,3,2]
    Output: 14
    Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
    2 * (2+3+2) = 2 * 7 = 14.
    ```

    ```
    Input: nums = [2,3,3,1,2]
    Output: 18
    Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
    3 * (3+3) = 3 * 6 = 18.
    ```

    ```
    Input: nums = [3,1,5,6,4,2]
    Output: 60
    Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
    4 * (5+6+4) = 4 * 15 = 60.
    ```

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `1 <= nums[i] <= 10^7`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_sum_min_product(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement max_sum_min_product')

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
