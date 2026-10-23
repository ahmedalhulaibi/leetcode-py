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
    # 628. Maximum Product of Three Numbers

    **Easy** · Array, Math, Sorting

    You are given an integer array `nums`.

    Find three numbers whose product is maximum and return the maximum product.

    ## Examples

    ```
    Input: nums = [1,2,3]
    Output: 6
    Explanation: The only three numbers are 1, 2, and 3, so the maximum product is 1 * 2 * 3 = 6.
    ```

    ```
    Input: nums = [1,2,3,4]
    Output: 24
    Explanation: The largest product comes from the three greatest numbers: 2 * 3 * 4 = 24.
    ```

    ```
    Input: nums = [-1,-2,-3]
    Output: -6
    Explanation: The only three numbers are -1, -2, and -3, so the maximum product is (-1) * (-2) * (-3) = -6.
    ```

    ## Constraints

    - `3 <= nums.length <= 10^4`
    - `-1000 <= nums[i] <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_product(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement maximum_product')

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
