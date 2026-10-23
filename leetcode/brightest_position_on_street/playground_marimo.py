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
    # 2021. Brightest Position on Street

    **Medium** · Array, Ordered Set, Prefix Sum, Sorting

    A perfectly straight street is represented by a number line. The street has `street lamp(s)` on it and is represented by a 2D integer array `lights`. Each `lights[i] = [position_i, range_i]` indicates that there is a street lamp at position `position_i` that lights up the area from `[position_i - range_i, position_i + range_i]` (**inclusive**).

    The **brightness** of a position `p` is defined as the number of street lamps that light up the position `p`.

    Given `lights`, return *the **brightest** position on the street*. If there are multiple brightest positions, return the **smallest** one.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/09/28/image-20210928155140-1.png)

    ```
    Input: lights = [[-3,2],[1,2],[3,3]]
    Output: -1
    Explanation:
    The first street lamp lights up the area from [(-3) - 2, (-3) + 2] = [-5, -1].
    The second street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].
    The third street lamp lights up the area from [3 - 3, 3 + 3] = [0, 6].

    Position -1 has a brightness of 2, illuminated by the first and second street light.
    Positions 0, 1, 2, and 3 have a brightness of 2, illuminated by the second and third street light.
    Out of all these positions, -1 is the smallest, so return it.
    ```

    ```
    Input: lights = [[1,0],[0,1]]
    Output: 1
    Explanation:
    The first street lamp lights up the area from [1 - 0, 1 + 0] = [1, 1].
    The second street lamp lights up the area from [0 - 1, 0 + 1] = [-1, 1].

    Position 1 has a brightness of 2, illuminated by the first and second street light.
    Return 1 because it is the brightest position on the street.
    ```

    ```
    Input: lights = [[1,2]]
    Output: -1
    Explanation:
    The first street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].

    Positions -1, 0, 1, 2, and 3 have a brightness of 1, illuminated by the first street light.
    Out of all these positions, -1 is the smallest, so return it.
    ```

    ## Constraints

    - 1 <= lights.length <= 10^5
    - lights[i].length == 2
    - -10^8 <= position_i <= 10^8
    - 0 <= range_i <= 10^8



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def brightest_position(self, lights: list[list[int]]) -> int:
            raise NotImplementedError('Implement brightest_position')

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
