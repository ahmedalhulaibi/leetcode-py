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
    # 661. Image Smoother

    **Easy** · Array, Matrix

    An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

    Given an `m x n` integer matrix `img` representing the grayscale of an image, return the image after applying the smoother on each cell of it.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/03/smooth-grid.jpg)

    ```
    Input: img = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[0,0,0],[0,0,0],[0,0,0]]
    Explanation: For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0.
    For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0.
    For the point (1,1): floor(8/9) = floor(0.88888889) = 0.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/05/03/smooth2-grid.jpg)

    ```
    Input: img = [[100,200,100],[200,50,200],[100,200,100]]
    Output: [[137,141,137],[141,138,141],[137,141,137]]
    Explanation: For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137.
    For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141.
    For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138.
    ```

    ## Constraints

    - m == img.length
    - n == img[i].length
    - 1 <= m, n <= 200
    - 0 <= img[i][j] <= 255



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def image_smoother(self, img: list[list[int]]) -> list[list[int]]:
            raise NotImplementedError('Implement image_smoother')

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
