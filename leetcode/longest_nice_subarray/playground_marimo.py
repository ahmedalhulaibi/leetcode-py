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
    # 2401. Longest Nice Subarray

    **Medium** · Array, Bit Manipulation, Sliding Window

    You are given an array `nums` consisting of positive integers.

    We call a subarray of `nums` nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

    Return the length of the longest nice subarray.

    A subarray is a contiguous part of an array.

    Note that subarrays of length 1 are always considered nice.

    ## Examples

    ```
    Input: nums = [1,3,8,48,10]
    Output: 3
    Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
    - 3 AND 8 = 0.
    - 3 AND 48 = 0.
    - 8 AND 48 = 0.
    It can be proven that no longer nice subarray can be obtained, so we return 3.
    ```

    ```
    Input: nums = [3,1,5,11,13]
    Output: 1
    Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
    ```

    ## Constraints

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def longest_nice_subarray(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement longest_nice_subarray')

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
