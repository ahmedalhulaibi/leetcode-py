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
    # 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

    **Easy** · Array

    You are given an array of integers `nums`. Return the length of the longest subarray of `nums` which is either strictly increasing or strictly decreasing.

    ## Examples

    ```
    Input: nums = [1,4,3,3,2]
    Output: 2
    Explanation:
    The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
    The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
    Hence, we return 2.
    ```

    ```
    Input: nums = [3,3,3,3]
    Output: 1
    Explanation:
    The strictly increasing subarrays of nums are [3], [3], [3], and [3].
    The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
    Hence, we return 1.
    ```

    ```
    Input: nums = [3,2,1]
    Output: 3
    Explanation:
    The strictly increasing subarrays of nums are [3], [2], and [1].
    The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
    Hence, we return 3.
    ```

    ## Constraints

    - 1 <= nums.length <= 50
    - 1 <= nums[i] <= 50



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def longest_monotonic_subarray(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement longest_monotonic_subarray')

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
