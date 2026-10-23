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
    # 1460. Make Two Arrays Equal by Reversing Subarrays

    **Easy** · Array, Hash Table, Sorting

    You are given two integer arrays of equal length `target` and `arr`. In one step, you can select any **non-empty subarray** of `arr` and reverse it. You are allowed to make any number of steps.

    Return `true` if you can make `arr` equal to `target` or `false` otherwise.

    ## Examples

    ```
    Input: target = [1,2,3,4], arr = [2,4,1,3]
    Output: true
    Explanation: You can follow the next steps to convert arr to target:
    1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
    2- Reverse subarray [4,2], arr becomes [1,2,4,3]
    3- Reverse subarray [4,3], arr becomes [1,2,3,4]
    There are multiple ways to convert arr to target, this is not the only way to do so.
    ```

    ```
    Input: target = [7], arr = [7]
    Output: true
    Explanation: arr is equal to target without any reverses.
    ```

    ```
    Input: target = [3,7,9], arr = [3,7,11]
    Output: false
    Explanation: arr does not have value 9 and it can never be converted to target.
    ```

    ## Constraints

    - target.length == arr.length
    - 1 <= target.length <= 1000
    - 1 <= target[i] <= 1000
    - 1 <= arr[i] <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_be_equal(self, target: list[int], arr: list[int]) -> bool:
            raise NotImplementedError('Implement can_be_equal')

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
