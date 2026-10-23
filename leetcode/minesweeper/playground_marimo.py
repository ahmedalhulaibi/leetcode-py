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
    # 529. Minesweeper

    **Medium** · Array, Depth-First Search, Breadth-First Search, Matrix

    Let's play the minesweeper game ([Wikipedia](https://en.wikipedia.org/wiki/Minesweeper_%28video_game%29), [online game](http://minesweeperonline.com))!

    You are given an `m x n` char matrix `board` representing the game board where:

    - `'M'` represents an unrevealed mine,
    - `'E'` represents an unrevealed empty square,
    - `'B'` represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
    - digit (`'1'` to `'8'`) represents how many mines are adjacent to this revealed square, and
    - `'X'` represents a revealed mine.

    You are also given an integer array `click` where `click = [clickr, clickc]` represents the next click position among all the unrevealed squares (`'M'` or `'E'`).

    Return *the board after revealing this position according to the following rules*:

    1. If a mine `'M'` is revealed, then the game is over. You should change it to `'X'`.
    2. If an empty square `'E'` with no adjacent mines is revealed, then change it to a revealed blank `'B'` and all of its adjacent unrevealed squares should be revealed recursively.
    3. If an empty square `'E'` with at least one adjacent mine is revealed, then change it to a digit (`'1'` to `'8'`) representing the number of adjacent mines.
    4. Return the board when no more squares will be revealed.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/08/09/untitled.jpeg)

    ```
    Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
    Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2023/08/09/untitled-2.jpeg)

    ```
    Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
    Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
    ```

    ## Constraints

    - `m == board.length`
    - `n == board[i].length`
    - `1 <= m, n <= 50`
    - `board[i][j]` is either `'M'`, `'E'`, `'B'`, or a digit from `'1'` to `'8'`.
    - `click.length == 2`
    - `0 <= clickr < m`
    - `0 <= clickc < n`
    - `board[clickr][clickc]` is either `'M'` or `'E'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def update_board(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
            raise NotImplementedError('Implement update_board')

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
