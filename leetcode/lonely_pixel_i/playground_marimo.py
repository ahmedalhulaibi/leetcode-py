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
    # 531. Lonely Pixel I

    **Medium** · Array, Hash Table, Matrix

    Given an `m x n` `picture` consisting of black `'B'` and white `'W'` pixels, return the number of **black** lonely pixels.

    A black lonely pixel is a character `'B'` located at a specific position where the same row and same column don't have **any other** black pixels.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0531.Lonely%20Pixel%20I/images/pixel1.jpg)

    ```
    Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
    Output: 3
    Explanation: All the three 'B's are black lonely pixels.
    ```

    ```
    Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
    Output: 0
    ```

    ## Constraints

    - `m == picture.length`
    - `n == picture[i].length`
    - `1 <= m, n <= 500`
    - `picture[i][j]` is `'W'` or `'B'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_lonely_pixel(self, picture: list[list[str]]) -> int:
            raise NotImplementedError('Implement find_lonely_pixel')

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
