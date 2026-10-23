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
    # 2001. Number of Pairs of Interchangeable Rectangles

    **Medium** · Array, Hash Table, Math, Counting, Number Theory

    You are given `n` rectangles represented as a **0-indexed** 2D integer array `rectangles`, where `rectangles[i] = [widthi, heighti]` denotes the width and height of the `ith` rectangle.

    Two rectangles `i` and `j` (`i < j`) are considered **interchangeable** if they have the **same** width-to-height ratio. More formally, two rectangles are **interchangeable** if `widthi / heighti == widthj / heightj` (using decimal division, not integer division).

    Return *the **number** of pairs of **interchangeable** rectangles* in `rectangles`.

    ## Examples

    ```
    Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
    Output: 6
    ```
    **Explanation:** The following are the interchangeable pairs of rectangles by index (0-indexed):
    - Rectangle 0 with rectangle 1: `4/8 == 3/6`.
    - Rectangle 0 with rectangle 2: `4/8 == 10/20`.
    - Rectangle 0 with rectangle 3: `4/8 == 15/30`.
    - Rectangle 1 with rectangle 2: `3/6 == 10/20`.
    - Rectangle 1 with rectangle 3: `3/6 == 15/30`.
    - Rectangle 2 with rectangle 3: `10/20 == 15/30`.

    ```
    Input: rectangles = [[4,5],[7,8]]
    Output: 0
    ```
    **Explanation:** There are no interchangeable pairs of rectangles.

    ## Constraints

    - `n == rectangles.length`
    - `1 <= n <= 10^5`
    - `rectangles[i].length == 2`
    - `1 <= widthi, heighti <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def interchangeable_rectangles(self, rectangles: list[list[int]]) -> int:
            raise NotImplementedError('Implement interchangeable_rectangles')

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
