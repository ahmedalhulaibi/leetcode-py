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
    # 593. Valid Square

    **Medium** · Math, Geometry

    Given the coordinates of four points in 2D space <code>p1</code>, <code>p2</code>, <code>p3</code> and <code>p4</code>, return <code>true</code> <em>if the four points construct a square</em>.

    <p>The coordinate of a point <code>p<sub>i</sub></code> is represented as <code>[x<sub>i</sub>, y<sub>i</sub>]</code>. The input is <strong>not</strong> given in any order.</p>

    <p>A <strong>valid square</strong> has four equal sides with positive length and four equal angles (90-degree angles).</p>

    ## Examples

    ```
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: true
    ```

    ```
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
    Output: false
    ```

    ```
    Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
    Output: true
    ```

    ## Constraints

    - p1.length == p2.length == p3.length == p4.length == 2
    - -10^4 <= xi, yi <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def valid_square(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
            raise NotImplementedError('Implement valid_square')

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
