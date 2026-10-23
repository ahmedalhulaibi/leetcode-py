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
    # 658. Find K Closest Elements

    **Medium** · Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)

    Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

    An integer `a` is closer to `x` than an integer `b` if:

    - `|a - x| < |b - x|`, or
    - `|a - x| == |b - x|` and `a < b`

    ## Examples

    ```
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]
    ```

    ```
    Input: arr = [1,1,2,3,4,5], k = 4, x = -1
    Output: [1,1,2,3]
    ```

    ## Constraints

    - `1 <= k <= arr.length`
    - `1 <= arr.length <= 10^4`
    - `arr` is sorted in **ascending** order.
    - `-10^4 <= arr[i], x <= 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[int]:
            raise NotImplementedError('Implement find_closest_elements')

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
