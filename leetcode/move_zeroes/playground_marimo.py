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
    # 283. Move Zeroes

    **Easy** · Array, Two Pointers

    Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

    **Note** that you must do this in-place without making a copy of the array.

    ## Examples

    ```
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Explanation: The array after moving zeroes becomes [1,3,12,0,0].
    ```

    ```
    Input: nums = [0]
    Output: [0]
    ```

    ## Constraints

    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1

    **Follow up:** Could you minimize the total number of operations done?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def move_zeroes(self, nums: list[int]) -> None:
            raise NotImplementedError('Implement move_zeroes')

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
