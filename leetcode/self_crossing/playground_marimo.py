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
    # 335. Self Crossing

    **Hard** · Array, Math, Geometry

    You are given an array of integers `distance`.

    You start at the point `(0, 0)` on an **X-Y plane,** and you move `distance[0]` meters to the north, then `distance[1]` meters to the west, `distance[2]` meters to the south, `distance[3]` meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

    Return `true` if your path crosses itself or `false` if it does not.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/12/21/11.jpg)

    ```
    Input: distance = [2,1,1,2]
    Output: true
    Explanation: The path crosses itself at the point (0, 1).
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/12/21/22.jpg)

    ```
    Input: distance = [1,2,3,4]
    Output: false
    Explanation: The path does not cross itself at any point.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2022/12/21/33.jpg)

    ```
    Input: distance = [1,1,1,2,1]
    Output: true
    Explanation: The path crosses itself at the point (0, 0).
    ```

    ## Constraints

    - 1 <= distance.length <= 10^5
    - 1 <= distance[i] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_self_crossing(self, distance: list[int]) -> bool:
            raise NotImplementedError('Implement is_self_crossing')

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
