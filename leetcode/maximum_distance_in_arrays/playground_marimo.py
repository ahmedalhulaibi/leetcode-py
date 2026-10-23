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
    # 624. Maximum Distance in Arrays

    **Medium** · Array, Greedy

    You are given `m` `arrays`, where each array is sorted in **ascending order**.

    You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `a` and `b` to be their absolute difference `|a - b|`.

    Return *the maximum distance*.

    ## Examples

    ```
    Input: arrays = [[1,2,3],[4,5],[1,2,3]]
    Output: 4
    Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
    ```

    ```
    Input: arrays = [[1],[1]]
    Output: 0
    ```

    ## Constraints

    - m == arrays.length
    - 2 <= m <= 10^5
    - 1 <= arrays[i].length <= 500
    - -10^4 <= arrays[i][j] <= 10^4
    - arrays[i] is sorted in ascending order.
    - There will be at most 10^5 integers in all the arrays.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_distance(self, arrays: list[list[int]]) -> int:
            raise NotImplementedError('Implement max_distance')

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
