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
    # 699. Falling Squares

    **Hard** · Array, Segment Tree, Ordered Set

    There are several squares being dropped onto the X-axis of a 2D plane.

    You are given a 2D integer array <code>positions</code> where <code>positions[i] = [left<sub>i</sub>, sideLength<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> square with a side length of <code>sideLength<sub>i</sub></code> that is dropped with its left edge aligned with X-coordinate <code>left<sub>i</sub></code>.

    Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands <strong>on the top side of another square</strong> or <strong>on the X-axis</strong>. A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved.

    After each square is dropped, you must record the <strong>height of the current tallest stack of squares</strong>.

    Return <em>an integer array </em><code>ans</code><em> where </em><code>ans[i]</code><em> represents the height described above after dropping the <code>i<sup>th</sup></code><em> square</em>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/04/28/fallingsq1-plane.jpg)

    ```
    Input: positions = [[1,2],[2,3],[6,1]]
    Output: [2,5,5]
    ```
    **Explanation:** After the first drop, the tallest stack is square 1 with a height of 2. After the second drop, the tallest stack is squares 1 and 2 with a height of 5. After the third drop, the tallest stack is still squares 1 and 2 with a height of 5. Thus, we return an answer of [2, 5, 5].

    ```
    Input: positions = [[100,100],[200,100]]
    Output: [100,100]
    ```
    **Explanation:** After the first drop, the tallest stack is square 1 with a height of 100. After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100. Thus, we return an answer of [100, 100]. Note that square 2 only brushes the right side of square 1, which does not count as landing on it.

    ## Constraints

    - `1 <= positions.length <= 1000`
    - `1 <= lefti <= 10^8`
    - `1 <= sideLengthi <= 10^6`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def falling_squares(self, positions: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement falling_squares')

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
