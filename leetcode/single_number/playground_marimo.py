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
    # 136. Single Number

    **Easy** · Array, Bit Manipulation

    Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.

    ## Examples

    ```
    Input: nums = [2,2,1]
    Output: 1
    ```

    ```
    Input: nums = [4,1,2,1,2]
    Output: 4
    ```

    ```
    Input: nums = [1]
    Output: 1
    ```

    ## Constraints

    - 1 <= nums.length <= 3 * 10^4
    - -3 * 10^4 <= nums[i] <= 3 * 10^4
    - Each element in the array appears twice except for one element which appears only once.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def single_number(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement single_number')

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
