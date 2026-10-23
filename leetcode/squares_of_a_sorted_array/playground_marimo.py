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
    # 977. Squares of a Sorted Array

    **Easy** · Array, Two Pointers, Sorting

    Given an integer array `nums` sorted in non-decreasing order, return *an array of the squares of each number* sorted in non-decreasing order.

    ## Examples

    ```
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]

    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
    ```

    ```
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
    ```

    ## Constraints

    - `1 <= nums.length <= 10^4`
    - `-10^4 <= nums[i] <= 10^4`
    - `nums` is sorted in non-decreasing order.

    **Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def sorted_squares(self, nums: list[int]) -> list[int]:
            raise NotImplementedError('Implement sorted_squares')

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
