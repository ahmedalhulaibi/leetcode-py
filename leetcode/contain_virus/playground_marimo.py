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
    # 749. Contain Virus

    **Hard** · Array, Depth-First Search, Breadth-First Search, Matrix, Simulation

    A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

    The world is modeled as an `m x n` binary grid `isInfected`, where `isInfected[i][j] == 0` represents uninfected cells, and `isInfected[i][j] == 1` represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two **4-directionally** adjacent cells, on the shared boundary.

    Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There **will never be a tie**.

    Return *the number of walls used to quarantine all the infected regions*. If the world will become fully infected, return the number of walls used.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/06/01/virus11-grid.jpg)

    ```
    Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
    Output: 10
    Explanation: There are 2 contaminated regions.
    On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
    ![Example 1 after day 1](https://assets.leetcode.com/uploads/2021/06/01/virus12edited-grid.jpg)
    On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
    ![Example 1 after day 2](https://assets.leetcode.com/uploads/2021/06/01/virus13edited-grid.jpg)
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/06/01/virus2-grid.jpg)

    ```
    Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
    Output: 4
    Explanation: Even though there is only one cell saved, there are 4 walls built.
    Notice that walls are only built on the shared boundary of two different cells.
    ```

    ```
    Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
    Output: 13
    Explanation: The region on the left only builds two new walls.
    ```

    ## Constraints

    - m == isInfected.length
    - n == isInfected[i].length
    - 1 <= m, n <= 50
    - isInfected[i][j] is either 0 or 1.
    - There is always a contiguous viral region throughout the described process that will infect strictly more uncontaminated squares in the next round.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def contain_virus(self, is_infected: list[list[int]]) -> int:
            raise NotImplementedError('Implement contain_virus')

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
