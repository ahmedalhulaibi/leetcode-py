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
    # 2965. Find Missing and Repeated Values

    **Easy** · Array, Hash Table, Math, Matrix

    You are given a 0-indexed 2D integer matrix `grid` of size `n * n` with values in the range `[1, n^2]`. Each integer appears exactly once except `a` which appears twice and `b` which is missing. The task is to find the repeating and missing numbers `a` and `b`.

    Return a 0-indexed integer array `ans` of size 2 where `ans[0]` equals to `a` and `ans[1]` equals to `b`.

    ## Examples

    ```
    Input: grid = [[1,3],[2,2]]
    Output: [2,4]
    Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
    ```

    ```
    Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
    Output: [9,5]
    Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
    ```

    ## Constraints

    - 2 <= n == grid.length == grid[i].length <= 50
    - 1 <= grid[i][j] <= n * n
    - For all x that 1 <= x <= n * n there is exactly one x that is not equal to any of the grid members.
    - For all x that 1 <= x <= n * n there is exactly one x that is equal to exactly two of the grid members.
    - For all x that 1 <= x <= n * n except two of them there is exactly one pair of i, j that 0 <= i, j <= n - 1 and grid[i][j] == x.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_missing_and_repeated_values(self, grid: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement find_missing_and_repeated_values')

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
