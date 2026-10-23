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
    # 978. Longest Turbulent Subarray

    **Medium** · Array, Dynamic Programming, Sliding Window

    Given an integer array `arr`, return *the length of a maximum size turbulent subarray of* `arr`.

    A subarray is **turbulent** if the comparison sign flips between each adjacent pair of elements in the subarray.

    More formally, a subarray `[arr[i], arr[i + 1], ..., arr[j]]` of `arr` is said to be turbulent if and only if:

    - For `i <= k < j`:
      - `arr[k] > arr[k + 1]` when `k` is odd, and
      - `arr[k] < arr[k + 1]` when `k` is even.
    - Or, for `i <= k < j`:
      - `arr[k] > arr[k + 1]` when `k` is even, and
      - `arr[k] < arr[k + 1]` when `k` is odd.

    ## Examples

    ```
    Input: arr = [9,4,2,10,7,8,8,1,9]
    Output: 5
    Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
    ```

    ```
    Input: arr = [4,8,12,16]
    Output: 2
    ```

    ```
    Input: arr = [100]
    Output: 1
    ```

    ## Constraints

    - 1 <= arr.length <= 4 * 10^4
    - 0 <= arr[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_turbulence_size(self, arr: list[int]) -> int:
            raise NotImplementedError('Implement max_turbulence_size')

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
