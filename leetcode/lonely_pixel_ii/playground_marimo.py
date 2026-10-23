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
    # 533. Lonely Pixel II

    **Medium** · Array, Hash Table, Matrix

    Given an `m x n` `picture` consisting of black `'B'` and white `'W'` pixels and an integer `target`, return the number of **black** lonely pixels.

    A black lonely pixel is a character `'B'` located at a specific position `(r, c)` where:

    - Row `r` and column `c` both contain exactly `target` black pixels.
    - For all rows that have a black pixel at column `c`, they should be exactly the same as row `r`.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0533.Lonely%20Pixel%20II/images/pixel2-1-grid.jpg)

    ```
    Input: picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3
    Output: 6
    Explanation: All the green 'B's are the black pixels we need (all 'B's at column 1 and 3).
    Take 'B' at row r = 0 and column c = 1 as an example:
     - Rule 1, row r = 0 and column c = 1 both have exactly target = 3 black pixels.
     - Rule 2, the rows that have a black pixel at column c = 1 are row 0, row 1 and row 2. They are exactly the same as row r = 0.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0533.Lonely%20Pixel%20II/images/pixel2-2-grid.jpg)

    ```
    Input: picture = [["W","W","B"],["W","W","B"],["W","W","B"]], target = 1
    Output: 0
    ```

    ## Constraints

    - `m == picture.length`
    - `n == picture[i].length`
    - `1 <= m, n <= 200`
    - `picture[i][j]` is `'W'` or `'B'`.
    - `1 <= target <= min(m, n)`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_black_pixel(self, picture: list[list[str]], target: int) -> int:
            raise NotImplementedError('Implement find_black_pixel')

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
