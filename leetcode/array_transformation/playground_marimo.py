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
    # 1243. Array Transformation

    **Easy** · Array, Simulation

    Given an initial array `arr`, every day you produce a new array using the array of the previous day.

    On the `i`-th day, you do the following operations on the array of day `i-1` to produce the array of day `i`:

    1. If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
    2. If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
    3. The first and last elements never change.

    After some days, the array does not change. Return that final array.

    ## Examples

    ```
    Input: arr = [6,2,3,4]
    Output: [6,3,3,4]
    ```
    **Explanation:** On the first day, the array is changed from `[6,2,3,4]` to `[6,3,3,4]`. No more operations can be done to this array.

    ```
    Input: arr = [1,6,3,4,3,5]
    Output: [1,4,4,4,4,5]
    ```
    **Explanation:** On the first day, the array is changed from `[1,6,3,4,3,5]` to `[1,5,4,3,4,5]`. On the second day, it is changed from `[1,5,4,3,4,5]` to `[1,4,4,4,4,5]`. No more operations can be done to this array.

    ## Constraints

    - `3 <= arr.length <= 100`
    - `1 <= arr[i] <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def transform_array(self, arr: list[int]) -> list[int]:
            raise NotImplementedError('Implement transform_array')

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
