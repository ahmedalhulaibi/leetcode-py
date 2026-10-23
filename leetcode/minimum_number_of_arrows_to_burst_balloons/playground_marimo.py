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
    # 452. Minimum Number of Arrows to Burst Balloons

    **Medium** · Array, Greedy, Sorting

    There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [x_start, x_end]` denotes a balloon whose **horizontal diameter** stretches between `x_start` and `x_end`. You do not know the exact y-coordinates of the balloons.

    Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `x_start` and `x_end` is **burst** by an arrow shot at `x` if `x_start <= x <= x_end`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

    Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all balloons*.

    ## Examples

    ```
    Input: points = [[10,16],[2,8],[1,6],[7,12]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
    - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
    - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
    ```

    ```
    Input: points = [[1,2],[3,4],[5,6],[7,8]]
    Output: 4
    Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
    ```

    ```
    Input: points = [[1,2],[2,3],[3,4],[4,5]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
    - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
    - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
    ```

    ## Constraints

    - `1 <= points.length <= 10^5`
    - `points[i].length == 2`
    - `-2^31 <= x_start < x_end <= 2^31 - 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_min_arrow_shots(self, points: list[list[int]]) -> int:
            raise NotImplementedError('Implement find_min_arrow_shots')

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
