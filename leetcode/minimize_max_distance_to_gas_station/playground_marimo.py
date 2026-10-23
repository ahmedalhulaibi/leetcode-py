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
    # 774. Minimize Max Distance to Gas Station

    **Hard** · Array, Binary Search

    You are given an integer array `stations` that represents the positions of the gas stations on the x-axis. You are also given an integer `k`.

    You should add `k` new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

    Let `penalty()` be the **maximum** distance between adjacent gas stations after adding the `k` new stations.

    Return the smallest possible value of `penalty()`. Answers within `10^-6` of the actual answer will be accepted.

    ## Examples

    ```
    Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
    Output: 0.50000
    ```

    ```
    Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
    Output: 14.00000
    ```

    ## Constraints

    - 10 <= stations.length <= 2000
    - 0 <= stations[i] <= 10^8
    - stations is sorted in a strictly increasing order.
    - 1 <= k <= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minmax_gas_dist(self, stations: list[int], k: int) -> float:
            raise NotImplementedError('Implement minmax_gas_dist')

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
