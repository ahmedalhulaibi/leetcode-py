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
    mo.md(r"""
    # 959. Regions Cut By Slashes

    **Medium** · Array, Hash Table, Depth-First Search, Breadth-First Search, Union Find, Matrix

    An `n x n` grid is composed of `1 x 1` squares where each `1 x 1` square consists of a `'/`', `'\`', or blank space `' `'. These characters divide the square into contiguous regions.

    Given the grid `grid` represented as a string array, return *the number of regions*.

    Note that backslash characters are escaped, so a `'\`' is represented as `'\\`'.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/12/15/1.png)

    ```
    Input: grid = [" /","/ "]
    Output: 2
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2018/12/15/2.png)

    ```
    Input: grid = [" /","  "]
    Output: 1
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2018/12/15/4.png)

    ```
    Input: grid = ["/\\","\\/"]
    Output: 5
    Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
    ```

    ## Constraints

    - `n == grid.length == grid[i].length`
    - `1 <= n <= 30`
    - `grid[i][j]` is either `'/`', `'\`', or `' `'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def regions_by_slashes(self, grid: list[str]) -> int:
            raise NotImplementedError('Implement regions_by_slashes')

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
