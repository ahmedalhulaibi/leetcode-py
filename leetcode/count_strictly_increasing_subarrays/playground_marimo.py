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
    # 2393. Count Strictly Increasing Subarrays

    **Medium** · Array, Math, Dynamic Programming

    You are given an array `nums` consisting of **positive** integers.

    Return *the number of **subarrays** of* `nums` *that are in **strictly increasing** order*.

    A **subarray** is a **contiguous** part of an array.

    ## Examples

    ```
    Input: nums = [1,3,5,4,4,6]
    Output: 10
    Explanation: The strictly increasing subarrays are the following:
    - Subarrays of length 1: [1], [3], [5], [4], [4], [6].
    - Subarrays of length 2: [1,3], [3,5], [4,6].
    - Subarrays of length 3: [1,3,5].
    The total number of subarrays is 6 + 3 + 1 = 10.
    ```

    ```
    Input: nums = [1,2,3,4,5]
    Output: 15
    Explanation: Every subarray is strictly increasing. There are 15 possible subarrays that we can take.
    ```

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `1 <= nums[i] <= 10^6`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_strictly_increasing(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement count_strictly_increasing')

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
