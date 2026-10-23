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
    # 2958. Length of Longest Subarray With at Most K Frequency

    **Medium** · Array, Hash Table, Sliding Window

    You are given an integer array `nums` and an integer `k`.

    The **frequency** of an element `x` is the number of times it occurs in an array.

    An array is called **good** if the frequency of each element in this array is **less than or equal** to `k`.

    Return *the length of the longest* **good** *subarray of* `nums`.

    A **subarray** is a contiguous non-empty sequence of elements within an array.

    ## Examples

    ```
    Input: nums = [1,2,3,1,2,3,1,2], k = 2
    Output: 6
    Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
    It can be shown that there are no good subarrays with length more than 6.
    ```

    ```
    Input: nums = [1,2,1,2,1,2,1,2], k = 1
    Output: 2
    Explanation: The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
    It can be shown that there are no good subarrays with length more than 2.
    ```

    ```
    Input: nums = [5,5,5,5,5,5,5], k = 4
    Output: 4
    Explanation: The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.
    It can be shown that there are no good subarrays with length more than 4.
    ```

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `1 <= nums[i] <= 10^9`
    - `1 <= k <= nums.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_subarray_length(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_subarray_length')

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
