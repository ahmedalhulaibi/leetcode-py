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
    # 1861. Rotating the Box

    **Medium** · Array, Two Pointers, Matrix

    You are given an `m x n` matrix of characters `boxGrid` representing a side-view of a box. Each cell of the box is one of the following:

    - A stone `'#'`
    - A stationary obstacle `'*'`
    - Empty `'.'`

    The box is rotated **90 degrees clockwise**, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity **does not** affect the obstacles' positions, and the inertia from the box's rotation **does not** affect the stones' horizontal positions.

    It is **guaranteed** that each stone in `boxGrid` rests on an obstacle, another stone, or the bottom of the box.

    Return *an* `n x m` *matrix representing the box after the rotation described above*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png)

    ```
    Input: boxGrid = [['#','.','#']]
    Output: [['.'],['#'],['#']]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png)

    ```
    Input: boxGrid = [['#','.','*','.'],['#','#','*','.']]
    Output: [['#','.'],['#','#'],['*','*'],['.','.']]
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png)

    ```
    Input: boxGrid = [['#','#','*','.','*','.'],['#','#','#','*','.','.'],['#','#','#','.','#','.']]
    Output: [['.','#','#'],['.','#','#'],['#','#','*'],['#','*','.'],['#','.','*'],['#','.','.']]
    ```

    ## Constraints

    - `m == boxGrid.length`
    - `n == boxGrid[i].length`
    - `1 <= m, n <= 500`
    - `boxGrid[i][j]` is either `'#'`, `'*'`, or `'.'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def rotate_the_box(self, box_grid: list[list[str]]) -> list[list[str]]:
            raise NotImplementedError('Implement rotate_the_box')

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
