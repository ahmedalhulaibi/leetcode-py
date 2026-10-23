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
    # 1272. Remove Interval

    **Medium** · Array

    A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form `[a, b)`. A real number `x` is in the set if one of its intervals `[a, b)` contains `x` (i.e. `a <= x < b`).

    You are given a **sorted** list of disjoint intervals `intervals` representing a set of real numbers as described above, where `intervals[i] = [ai, bi]` represents the interval `[ai, bi)`. You are also given another interval `toBeRemoved`.

    Return *the set of real numbers with the interval* `toBeRemoved` *removed* from* `intervals`*. In other words, return the set of real numbers such that every `x` in the set is in `intervals` but **not** in `toBeRemoved`. Your answer should be a **sorted** list of disjoint intervals as described above.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1272.Remove%20Interval/images/removeintervalex1.png)

    ```
    Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
    Output: [[0,1],[6,7]]
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1272.Remove%20Interval/images/removeintervalex2.png)

    ```
    Input: intervals = [[0,5]], toBeRemoved = [2,3]
    Output: [[0,2],[3,5]]
    ```

    ```
    Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
    Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
    ```

    ## Constraints

    - 1 <= intervals.length <= 10^4
    - -10^9 <= ai < bi <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def remove_interval(self, intervals: list[list[int]], to_be_removed: list[int]) -> list[list[int]]:
            raise NotImplementedError('Implement remove_interval')

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
