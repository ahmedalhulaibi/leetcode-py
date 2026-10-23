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
    # 1121. Divide Array Into Increasing Sequences

    **Hard** · Array, Greedy

    Given an integer array `nums` sorted in **non-decreasing** order and an integer `k`, return `true` if this array can be divided into one or more disjoint **increasing** subsequences of length at least `k`, or `false` otherwise.

    ## Examples

    ```
    Input: nums = [1,2,2,3,3,4,4], k = 3
    Output: true
    Explanation: The array can be divided into two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
    ```

    ```
    Input: nums = [5,6,6,7,8], k = 3
    Output: false
    Explanation: There is no way to divide the array using the conditions required.
    ```

    ## Constraints

    - 1 <= k <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^5
    - nums is sorted in non-decreasing order.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_divide_into_subsequences(self, nums: list[int], k: int) -> bool:
            raise NotImplementedError('Implement can_divide_into_subsequences')

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
