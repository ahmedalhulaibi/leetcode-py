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
    # 780. Reaching Points

    **Hard** · Math, Euclidean Algorithm, Greatest Common Divisor

    Given four integers `sx`, `sy`, `tx`, and `ty`, return `true` if it is possible to convert the point `(sx, sy)` to the point `(tx, ty)` through some operations, or `false` otherwise.

    The allowed operation on some point `(x, y)` is to convert it to either `(x, x + y)` or `(x + y, y)`.

    ## Examples

    ```
    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: true
    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)
    ```

    ```
    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: false
    ```

    ```
    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: true
    ```

    ## Constraints

    - 1 <= sx, sy, tx, ty <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def reaching_points(self, sx: int, sy: int, tx: int, ty: int) -> bool:
            raise NotImplementedError('Implement reaching_points')

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
