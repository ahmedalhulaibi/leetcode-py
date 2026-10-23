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
    # 356. Line Reflection

    **Medium** · Array, Hash Table, Math

    Given `n` points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

    In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

    **Note** that there can be repeated points.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0356.Line%20Reflection/images/356_example_1.png)

    ```
    Input: points = [[1,1],[-1,1]]
    Output: true
    Explanation: We can choose the line x = 0.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0356.Line%20Reflection/images/356_example_2.png)

    ```
    Input: points = [[1,1],[-1,-1]]
    Output: false
    Explanation: We can't choose a line.
    ```

    ## Constraints

    - `n == points.length`
    - `1 <= n <= 10^4`
    - `-10^8 <= points[i][j] <= 10^8`

    **Follow up:** Could you do better than `O(n^2)`?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_reflected(self, points: list[list[int]]) -> bool:
            raise NotImplementedError('Implement is_reflected')

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
