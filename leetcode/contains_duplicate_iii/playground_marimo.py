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
    # 220. Contains Duplicate III

    **Hard** · Array, Sliding Window, Sorting, Bucket Sort, Ordered Set

    You are given an integer array `nums` and two integers `indexDiff` and `valueDiff`.

    Find a pair of indices `(i, j)` such that:

    - `i != j`,
    - `abs(i - j) <= indexDiff`, and
    - `abs(nums[i] - nums[j]) <= valueDiff`.

    Return `true` *if such pair exists or* `false` *otherwise*.

    ## Examples

    ```
    Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
    Output: true
    Explanation: We can choose (i, j) = (0, 3).
    i != j, abs(i - j) <= indexDiff, abs(nums[i] - nums[j]) <= valueDiff
    ```

    ```
    Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
    Output: false
    Explanation: No pair of indices satisfies all three conditions.
    ```

    ## Constraints

    - 2 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - 1 <= indexDiff <= nums.length
    - 0 <= valueDiff <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def contains_nearby_almost_duplicate(self, nums: list[int], index_diff: int, value_diff: int) -> bool:
            raise NotImplementedError('Implement contains_nearby_almost_duplicate')

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
