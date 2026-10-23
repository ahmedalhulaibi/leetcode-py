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
    # 813. Largest Sum of Averages

    **Medium** · Array, Dynamic Programming, Prefix Sum

    You are given an integer array `nums` and an integer `k`. You can partition the array into at most `k` non-empty adjacent subarrays. The **score** of a partition is the sum of the averages of each subarray.

    Note that the partition must use every integer in `nums`, and that the score is not necessarily an integer.

    Return the maximum **score** you can achieve of all the possible partitions. Answers within `10^-6` of the actual answer will be accepted.

    ## Examples

    ```
    Input: nums = [9,1,2,3,9], k = 3
    Output: 20.00000
    Explanation: The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
    ```

    ```
    Input: nums = [1,2,3,4,5,6,7], k = 4
    Output: 20.50000
    ```

    ## Constraints

    - `1 <= nums.length <= 100`
    - `1 <= nums[i] <= 10^4`
    - `1 <= k <= nums.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def largest_sum_of_averages(self, nums: list[int], k: int) -> float:
            raise NotImplementedError('Implement largest_sum_of_averages')

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
