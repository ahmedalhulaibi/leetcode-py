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
    # 302. Smallest Rectangle Enclosing Black Pixels

    **Hard** · Depth-First Search, Breadth-First Search, Array, Binary Search, Matrix

    You are given an `m x n` binary matrix `image` where `0` represents a white pixel and `1` represents a black pixel.

    The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

    Given two integers `x` and `y` that represents the location of one of the black pixels, return *the area of the smallest (axis-aligned) rectangle that encloses all black pixels*.

    You must write an algorithm with less than `O(mn)` runtime complexity.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0302.Smallest%20Rectangle%20Enclosing%20Black%20Pixels/images/pixel-grid.jpg)

    ```
    Input: image = [["0010"],["0110"],["0100"]], x = 0, y = 2
    Output: 6
    ```

    ```
    Input: image = [["1"]], x = 0, y = 0
    Output: 1
    ```

    ## Constraints

    - `m == image.length`
    - `n == image[i].length`
    - `1 <= m, n <= 100`
    - `image[i][j]` is either `'0'` or `'1'`.
    - `0 <= x < m`
    - `0 <= y < n`
    - `image[x][y] == '1'`.
    - The black pixels in the `image` only form **one component**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_area(self, image: list[list[str]], x: int, y: int) -> int:
            raise NotImplementedError('Implement min_area')

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
