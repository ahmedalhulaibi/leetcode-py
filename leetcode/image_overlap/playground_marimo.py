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
    # 835. Image Overlap

    **Medium** · Array, Matrix

    You are given two images, `img1` and `img2`, represented as binary, square matrices of size `n x n`. A binary matrix has only `0`s and `1`s as values.

    We **translate** one image however we choose by sliding all the `1` bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the **overlap** by counting the number of positions that have a `1` in **both** images.

    Note also that a translation does **not** include any kind of rotation. Any `1` bits that are translated outside of the matrix borders are erased.

    Return *the largest possible overlap*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg)

    ```
    Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
    Output: 3
    Explanation: We translate img1 to right by 1 unit and down by 1 unit.
    ```

    ![Step 1](https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg)

    The number of positions that have a 1 in both images is 3 (shown in red).

    ![Step 2](https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg)

    ```
    Input: img1 = [[1]], img2 = [[1]]
    Output: 1
    ```

    ```
    Input: img1 = [[0]], img2 = [[0]]
    Output: 0
    ```

    ## Constraints

    - n == img1.length == img1[i].length
    - n == img2.length == img2[i].length
    - 1 <= n <= 30
    - img1[i][j] is either 0 or 1.
    - img2[i][j] is either 0 or 1.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def largest_overlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
            raise NotImplementedError('Implement largest_overlap')

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
