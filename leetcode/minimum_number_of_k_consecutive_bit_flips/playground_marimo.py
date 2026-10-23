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
    # 995. Minimum Number of K Consecutive Bit Flips

    **Hard** · Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum

    You are given a binary array `nums` and an integer `k`.

    A **k-bit flip** is choosing a **subarray** of length `k` from `nums` and **simultaneously** changing every `0` in the subarray to `1`, and every `1` in the subarray to `0`.

    Return *the minimum number of `k-bit` flips required so that there is no `0` in the array.* If it is not possible, return `-1`.

    A subarray is a **contiguous** part of an array.

    ## Examples

    ```
    Input: nums = [0,1,0], k = 1
    Output: 2
    Explanation: Flip nums[0], then flip nums[2].
    ```

    ```
    Input: nums = [1,1,0], k = 2
    Output: -1
    Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
    ```

    ```
    Input: nums = [0,0,0,1,0,1,1,0], k = 3
    Output: 3
    Explanation:
    Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
    Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
    Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
    ```

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `1 <= k <= nums.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_k_bit_flips(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement min_k_bit_flips')

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
