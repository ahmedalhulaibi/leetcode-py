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
    # 754. Reach a Number

    **Medium** · Math, Binary Search

    You are standing at position `0` on an infinite number line. There is a destination at position `target`.

    You can make some number of moves `numMoves` so that:

    - On each move, you can either go left or right.
    - During the `i^th` move (starting from `i == 1` to `i == numMoves`), you take `i` steps in the chosen direction.

    Given the integer `target`, return *the **minimum** number of moves required (i.e., the minimum `numMoves`)* to reach the destination.

    ## Examples

    ```
    Input: target = 2
    Output: 3
    Explanation:
    On the 1st move, we step from 0 to 1 (1 step).
    On the 2nd move, we step from 1 to -1 (2 steps).
    On the 3rd move, we step from -1 to 2 (3 steps).
    ```

    ```
    Input: target = 3
    Output: 2
    Explanation:
    On the 1st move, we step from 0 to 1 (1 step).
    On the 2nd move, we step from 1 to 3 (2 steps).
    ```

    ## Constraints

    - `-10^9 <= target <= 10^9`
    - `target != 0`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def reach_number(self, target: int) -> int:
            raise NotImplementedError('Implement reach_number')

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
