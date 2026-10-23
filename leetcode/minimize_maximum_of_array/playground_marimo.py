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
    # 2439. Minimize Maximum of Array

    **Medium** · Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum

    You are given a 0-indexed array `nums` comprising of `n` non-negative integers.

    In one operation, you must:

    - Choose an integer `i` such that `1 <= i < n` and `nums[i] > 0`.
    - Decrease `nums[i]` by 1.
    - Increase `nums[i - 1]` by 1.

    Return *the **minimum** possible value of the **maximum** integer of* `nums` *after performing **any** number of operations*.

    ## Examples

    ```
    Input: nums = [3,7,1,6]
    Output: 5
    Explanation:
    One set of optimal operations is as follows:
    1. Choose i = 1, and nums becomes [4,6,1,6].
    2. Choose i = 3, and nums becomes [4,6,2,5].
    3. Choose i = 1, and nums becomes [5,5,2,5].
    The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
    Therefore, we return 5.
    ```

    ```
    Input: nums = [10,1]
    Output: 10
    Explanation:
    It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
    ```

    ## Constraints

    - n == nums.length
    - 2 <= n <= 10^5
    - 0 <= nums[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimize_array_value(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement minimize_array_value')

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
