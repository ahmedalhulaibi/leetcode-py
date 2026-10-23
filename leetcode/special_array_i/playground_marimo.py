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
    # 3151. Special Array I

    **Easy** · Array

    An array is considered **special** if the **parity** of every pair of adjacent elements is different. In other words, one element in each pair **must** be even, and the other **must** be odd.

    You are given an array of integers `nums`. Return `true` if `nums` is a **special** array, otherwise, return `false`.

    ## Examples

    ```
    Input: nums = [1]
    Output: true
    Explanation: There is only one element. So the answer is true.
    ```

    ```
    Input: nums = [2,1,4]
    Output: true
    Explanation: There are two pairs: (2,1) and (1,4), and both contain numbers with different parity.
    ```

    ```
    Input: nums = [4,3,1,6]
    Output: false
    Explanation: nums[1] and nums[2] are both odd. So the answer is false.
    ```

    ## Constraints

    - `1 <= nums.length <= 100`
    - `1 <= nums[i] <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_array_special(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement is_array_special')

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
