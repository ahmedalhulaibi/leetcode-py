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
    # 2369. Check if There is a Valid Partition For The Array

    **Medium** · Array, Dynamic Programming

    You are given a **0-indexed** integer array `nums`. You have to partition the array into one or more **contiguous** subarrays.

    We call a partition of the array **valid** if each of the obtained subarrays satisfies **one** of the following conditions:

    - The subarray consists of **exactly** 2, equal elements. For example, the subarray `[2,2]` is good.
    - The subarray consists of **exactly** 3, equal elements. For example, the subarray `[4,4,4]` is good.
    - The subarray consists of **exactly** 3 consecutive increasing elements, that is, the difference between adjacent elements is `1`. For example, the subarray `[3,4,5]` is good, but the subarray `[1,3,5]` is not.

    Return `true` *if the array has **at least** one valid partition*. Otherwise, return `false`.

    ## Examples

    ```
    Input: nums = [4,4,4,5,6]
    Output: true
    Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
    This partition is valid, so we return true.
    ```

    ```
    Input: nums = [1,1,1,2]
    Output: false
    Explanation: There is no valid partition for this array.
    ```

    ## Constraints

    - 2 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def valid_partition(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement valid_partition')

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
