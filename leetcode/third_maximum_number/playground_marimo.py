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
    # 414. Third Maximum Number

    **Easy** · Array, Sorting

    You are given an integer array `nums`.

    Return the third **distinct maximum** number in this array. If the third **maximum** does not exist, return the **maximum** number.

    ## Examples

    ```
    Input: nums = [3,2,1]
    Output: 1
    ```
    **Explanation:** The first distinct maximum is 3. The second distinct maximum is 2. The third distinct maximum is 1.

    ```
    Input: nums = [1,2]
    Output: 2
    ```
    **Explanation:** The first distinct maximum is 2. The second distinct maximum is 1. The third maximum does not exist, so the maximum (2) is returned instead.

    ```
    Input: nums = [2,2,3,1]
    Output: 1
    ```
    **Explanation:** The first distinct maximum is 3. The second distinct maximum is 2 (both 2's are counted together since they have the same value). The third distinct maximum is 1.

    ## Constraints

    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1

    **Follow up:** Can you find an `O(n)` solution?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def third_max(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement third_max')

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
