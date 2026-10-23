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
    # 1685. Sum of Absolute Differences in a Sorted Array

    **Medium** · Array, Math, Prefix Sum

    You are given an integer array `nums` sorted in **non-decreasing** order.

    Build and return *an integer array* `result` *with the same length as* `nums` *such that* `result[i]` *is equal to the* ***summation of absolute differences*** *between* `nums[i]` *and all the other elements in the array.*

    In other words, `result[i]` is equal to `sum(|nums[i]-nums[j]|)` where `0 <= j < nums.length` and `j != i` (**0-indexed**).

    ## Examples

    ```
    Input: nums = [2,3,5]
    Output: [4,3,5]
    Explanation: Assuming the arrays are 0-indexed, then
    result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
    result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
    result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
    ```

    ```
    Input: nums = [1,4,6,8,10]
    Output: [24,15,13,15,21]
    ```

    ## Constraints

    - 2 <= nums.length <= 10^5
    - 1 <= nums[i] <= nums[i + 1] <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_sum_absolute_differences(self, nums: list[int]) -> list[int]:
            raise NotImplementedError('Implement get_sum_absolute_differences')

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
