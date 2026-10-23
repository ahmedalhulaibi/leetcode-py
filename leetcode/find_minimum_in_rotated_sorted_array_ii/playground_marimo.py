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
    # 154. Find Minimum in Rotated Sorted Array II

    **Hard** · Array, Binary Search

    Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,4,4,5,6,7]` might become:

    - `[4,5,6,7,0,1,4]` if it was rotated `4` times.
    - `[0,1,4,4,5,6,7]` if it was rotated `7` times.

    Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

    Given the sorted rotated array `nums` that may contain **duplicates**, return *the minimum element of this array*.

    You must decrease the overall operation steps as much as possible.

    ## Examples

    ```
    Input: nums = [1,3,5]
    Output: 1
    ```

    ```
    Input: nums = [2,2,2,0,1]
    Output: 0
    ```

    ## Constraints

    - n == nums.length
    - 1 <= n <= 5000
    - -5000 <= nums[i] <= 5000
    - nums is sorted and rotated between 1 and n times.

    **Follow up:** This problem is similar to Find Minimum in Rotated Sorted Array, but `nums` may contain duplicates. Would this affect the runtime complexity? How and why?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_min(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement find_min')

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
