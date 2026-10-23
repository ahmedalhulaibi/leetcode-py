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
    # 1043. Partition Array for Maximum Sum

    **Medium** · Array, Dynamic Programming

    Given an integer array `arr`, partition the array into (contiguous) subarrays of length **at most** `k`. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

    Return *the largest sum of the given array after partitioning*. Test cases are generated so that the answer fits in a **32-bit** integer.

    ## Examples

    ```
    Input: arr = [1,15,7,9,2,5,10], k = 3
    Output: 84
    Explanation: arr becomes [15,15,15,9,10,10,10]
    ```

    ```
    Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
    Output: 83
    ```

    ```
    Input: arr = [1], k = 1
    Output: 1
    ```

    ## Constraints

    - `1 <= arr.length <= 500`
    - `0 <= arr[i] <= 10^9`
    - `1 <= k <= arr.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_sum_after_partitioning(self, arr: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_sum_after_partitioning')

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
