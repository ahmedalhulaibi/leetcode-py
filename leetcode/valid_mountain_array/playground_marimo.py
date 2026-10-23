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
    # 941. Valid Mountain Array

    **Easy** · Array

    Given an array of integers `arr`, return `true` if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:

    - `arr.length >= 3`
    - There exists some `i` with `0 < i < arr.length - 1` such that:
      - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
      - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

    ![Example](https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png)

    ## Examples

    ```
    Input: arr = [2,1]
    Output: false
    ```

    ```
    Input: arr = [3,5,5]
    Output: false
    ```

    ```
    Input: arr = [0,3,2,1]
    Output: true
    ```

    ## Constraints

    - 1 <= arr.length <= 10^4
    - 0 <= arr[i] <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def valid_mountain_array(self, arr: list[int]) -> bool:
            raise NotImplementedError('Implement valid_mountain_array')

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
