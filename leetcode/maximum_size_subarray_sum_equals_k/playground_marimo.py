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
    # 325. Maximum Size Subarray Sum Equals k

    **Medium** · Array, Hash Table, Prefix Sum

    Given an integer array `nums` and an integer `k`, return *the maximum length of a* subarray *that sums to* `k`. If there is not one, return `0` instead.

    ## Examples

    ```
    Input: nums = [1,-1,5,-2,3], k = 3
    Output: 4
    Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
    ```

    ```
    Input: nums = [-2,-1,2,1], k = 1
    Output: 2
    Explanation: The subarray [-1, 2] sums to 1 and is the longest.
    ```

    ## Constraints

    - `1 <= nums.length <= 2 * 10^5`
    - `-10^4 <= nums[i] <= 10^4`
    - `-10^9 <= k <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_sub_array_len(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_sub_array_len')

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
