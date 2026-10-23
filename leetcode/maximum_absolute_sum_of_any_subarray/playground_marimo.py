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
    # 1749. Maximum Absolute Sum of Any Subarray

    **Medium** · Array, Dynamic Programming

    You are given an integer array `nums`. The **absolute sum** of a subarray `[nums_l, nums_l+1, ..., nums_r-1, nums_r]` is `abs(nums_l + nums_l+1 + ... + nums_r-1 + nums_r)`.

    Return the maximum absolute sum of any (possibly empty) subarray of `nums`.

    Note that `abs(x)` is defined as follows:

    - If `x` is a negative integer, then `abs(x) = -x`.
    - If `x` is a non-negative integer, then `abs(x) = x`.

    ## Examples

    ```
    Input: nums = [1,-3,2,3,-4]
    Output: 5
    ```
    **Explanation:** The subarray `[2,3]` has absolute sum = abs(2+3) = abs(5) = 5.

    ```
    Input: nums = [2,-5,1,-4,3,-2]
    Output: 8
    ```
    **Explanation:** The subarray `[-5,1,-4]` has absolute sum = abs(-5+1-4) = abs(-8) = 8.

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `-10^4 <= nums[i] <= 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_absolute_sum(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement max_absolute_sum')

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
