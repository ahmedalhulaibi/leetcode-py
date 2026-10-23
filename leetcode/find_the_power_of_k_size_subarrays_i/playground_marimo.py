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
    # 3254. Find the Power of K-Size Subarrays I

    **Medium** · Array, Sliding Window

    You are given an array of integers `nums` of length `n` and a *positive* integer `k`.

    The **power** of an array is defined as:

    - Its **maximum** element if **all** of its elements are **consecutive** and **sorted** in **ascending** order.
    - `-1` otherwise.

    You need to find the **power** of all subarrays of `nums` of size `k`.

    Return an integer array `results` of size `n - k + 1`, where `results[i]` is the power of `nums[i..(i + k - 1)]`.

    ## Examples

    ```
    Input: nums = [1,2,3,4,3,2,5]
    Output: [3,4,-1,-1,-1]
    Explanation:
    There are 5 subarrays of nums of size 3:
    - [1, 2, 3] with the maximum element 3.
    - [2, 3, 4] with the maximum element 4.
    - [3, 4, 3] whose elements are not consecutive.
    - [4, 3, 2] whose elements are not sorted.
    - [3, 2, 5] whose elements are not consecutive.
    ```

    ```
    Input: nums = [2,2,2,2,2]
    Output: [-1,-1]
    ```

    ```
    Input: nums = [3,2,3,2,3,2]
    Output: [-1,3,-1,3,-1]
    ```

    ## Constraints

    - `1 <= n == nums.length <= 500`
    - `1 <= nums[i] <= 10^5`
    - `1 <= k <= n`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def results_array(self, nums: list[int], k: int) -> list[int]:
            raise NotImplementedError('Implement results_array')

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
