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
    # 927. Three Equal Parts

    **Hard** · Array, Math

    You are given an array `arr` which consists of only zeros and ones, divide the array into **three non-empty parts** such that all of these parts represent the same binary value.

    If it is possible, return any `[i, j]` with `i + 1 < j`, such that:

    - `arr[0], arr[1], ..., arr[i]` is the first part,
    - `arr[i + 1], arr[i + 2], ..., arr[j - 1]` is the second part, and
    - `arr[j], arr[j + 1], ..., arr[arr.length - 1]` is the third part.
    - All three parts have equal binary values.

    If it is not possible, return `[-1, -1]`.

    Note that the entire part is used when considering what binary value it represents. For example, `[1,1,0]` represents `6` in decimal, not `3`. Also, leading zeros **are allowed**, so `[0,1,1]` and `[1,1]` represent the same value.

    ## Examples

    ```
    Input: arr = [1,0,1,0,1]
    Output: [0,3]
    Explanation: The following figure shows a possible split of the array into three parts.
    ```

    ```
    Input: arr = [1,1,0,1,1]
    Output: [-1,-1]
    ```

    ```
    Input: arr = [1,1,0,0,1]
    Output: [0,2]
    ```

    ## Constraints

    - `3 <= arr.length <= 3 * 10^4`
    - `arr[i]` is `0` or `1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def three_equal_parts(self, arr: list[int]) -> list[int]:
            raise NotImplementedError('Implement three_equal_parts')

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
