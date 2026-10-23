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
    # 594. Longest Harmonious Subsequence

    **Easy** · Array, Hash Table, Sliding Window, Sorting, Counting

    We define a harmonious array as an array where the difference between its maximum value and its minimum value is **exactly** `1`.

    Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible subsequences.

    ## Examples

    ```
    Input: nums = [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].
    ```

    ```
    Input: nums = [1,2,3,4]
    Output: 2
    Explanation: The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.
    ```

    ```
    Input: nums = [1,1,1,1]
    Output: 0
    Explanation: No harmonious subsequence exists.
    ```

    ## Constraints

    - 1 <= nums.length <= 2 * 10^4
    - -10^9 <= nums[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_lhs(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement find_lhs')

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
