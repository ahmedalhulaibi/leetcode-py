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
    # 573. Squirrel Simulation

    **Medium** · Array, Math

    You are given two integers `height` and `width` representing a garden of size `height x width`. You are also given:

    - an array `tree` where `tree = [tree_r, tree_c]` is the position of the tree in the garden,
    - an array `squirrel` where `squirrel = [squirrel_r, squirrel_c]` is the position of the squirrel in the garden,
    - and an array `nuts` where `nuts[i] = [nut_i_r, nut_i_c]` is the position of the `i^th` nut in the garden.

    The squirrel can only take at most one nut at one time and can move in four directions: up, down, left, and right, to the adjacent cell.

    Return *the **minimal distance** for the squirrel to collect all the nuts and put them under the tree one by one*.

    The **distance** is the number of moves.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0573.Squirrel%20Simulation/images/squirrel1-grid.jpg)

    ```
    Input: height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]
    Output: 12
    ```
    **Explanation:** The squirrel should go to the nut at [2, 5] first to achieve a minimal distance.

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0573.Squirrel%20Simulation/images/squirrel2-grid.jpg)

    ```
    Input: height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]
    Output: 3
    ```

    ## Constraints

    - `1 <= height, width <= 100`
    - `tree.length == 2`
    - `squirrel.length == 2`
    - `1 <= nuts.length <= 5000`
    - `nuts[i].length == 2`
    - `0 <= tree_r, squirrel_r, nut_i_r <= height`
    - `0 <= tree_c, squirrel_c, nut_i_c <= width`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_distance(self, height: int, width: int, tree: list[int], squirrel: list[int], nuts: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_distance')

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
