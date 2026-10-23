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
    # 1228. Missing Number In Arithmetic Progression

    **Easy** · Array, Math

    In some array `arr`, the values were in arithmetic progression: the values `arr[i + 1] - arr[i]` are all equal for every `0 <= i < arr.length - 1`.

    A value from `arr` was removed that **was not the first or last value in the array**.

    Given `arr`, return *the removed value*.

    ## Examples

    ```
    Input: arr = [5,7,11,13]
    Output: 9
    Explanation: The previous array was [5,7,9,11,13].
    ```

    ```
    Input: arr = [15,13,12]
    Output: 14
    Explanation: The previous array was [15,14,13,12].
    ```

    ## Constraints

    - 3 <= arr.length <= 1000
    - 0 <= arr[i] <= 10^5
    - The given array is **guaranteed** to be a valid array.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def missing_number(self, arr: list[int]) -> int:
            raise NotImplementedError('Implement missing_number')

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
