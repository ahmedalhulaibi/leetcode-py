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
    # 852. Peak Index in a Mountain Array

    **Medium** · Array, Binary Search, Ternary Search

    You are given an integer **mountain** array `arr` of length `n` where the values increase to a **peak element** and then decrease.

    Return the index of the peak element.

    Your task is to solve it in `O(log(n))` time complexity.

    ## Examples

    ```
    Input: arr = [0,1,0]
    Output: 1
    ```

    ```
    Input: arr = [0,2,1,0]
    Output: 1
    ```

    ```
    Input: arr = [0,10,5,2]
    Output: 1
    ```

    ## Constraints

    - 3 <= arr.length <= 10^5
    - 0 <= arr[i] <= 10^6
    - arr is guaranteed to be a mountain array.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def peak_index_in_mountain_array(self, arr: list[int]) -> int:
            raise NotImplementedError('Implement peak_index_in_mountain_array')

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
