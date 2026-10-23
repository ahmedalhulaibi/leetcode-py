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
    # 909. Snakes and Ladders

    **Medium** · Array, Breadth-First Search, Matrix

    You are given an <code>n x n</code> integer matrix <code>board</code> where the cells are labeled from <code>1</code> to <code>n<sup>2</sup></code> in a <a href="https://en.wikipedia.org/wiki/Boustrophedon" target="_blank"><strong>Boustrophedon style</strong></a> starting from the bottom left of the board (i.e. <code>board[n - 1][0]</code>) and alternating direction each row.</p>

    <p>You start on square <code>1</code> of the board. In each move, starting from square <code>curr</code>, do the following:</p>

    <ul>
        <li>Choose a destination square <code>next</code> with a label in the range <code>[curr + 1, min(curr + 6, n<sup>2</sup>)]</code>.
        <ul>
            <li>This choice simulates the result of a standard <strong>6-sided die roll</strong>: i.e., there are always at most 6 destinations, regardless of the size of the board.</li>
        </ul>
        </li>
        <li>If <code>next</code> has a snake or ladder, you <strong>must</strong> move to the destination of that snake or ladder. Otherwise, you move to <code>next</code>.</li>
        <li>The game ends when you reach the square <code>n<sup>2</sup></code>.</li>
    </ul>

    <p>A board square on row <code>r</code> and column <code>c</code> has a snake or ladder if <code>board[r][c] != -1</code>. The destination of that snake or ladder is <code>board[r][c]</code>. Squares <code>1</code> and <code>n<sup>2</sup></code> are not the starting points of a snake or ladder.</p>

    <p>Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do <strong>not</strong> follow the subsequent snake or ladder.</p>

    <ul>
        <li>For example, suppose the board is <code>[[-1,4],[-1,3]]</code>, and on the first move, your destination square is <code>2</code>. You follow the ladder at square <code>2</code> to square <code>3</code>, but do <strong>not</strong> follow the subsequent ladder at square <code>3</code> to square <code>4</code>.</li>
    </ul>

    <p>Return <em>the least number of dice rolls required to reach the square</em> <code>n<sup>2</sup></code><em>. If it is not possible to reach the square, return</em> <code>-1</code>.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/09/23/snakes.png)

    ```
    Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    Output: 4
    Explanation:
    In the beginning, you start at square 1 = [5,0].
    You decide to move to square 2 = [5,1], and must take the ladder at square 2 to go to square 15 = [3,0].
    You decide to move to square 17 = [3,4], and must take the snake at square 17 to go to square 13 = [3,1].
    You decide to move to square 18 = [3,5], and must take the board at square 18 to go to square 36 = [0,5].
    You have 4 dice rolls to reach square 36, so return 4.
    ```

    ```
    Input: board = [[-1,-1],[-1,3]]
    Output: 1
    ```

    ## Constraints

    - n == board.length == board[i].length
    - 2 <= n <= 20
    - board[i][j] is either -1 or in the range [1, n^2].
    - The squares labeled 1 and n^2 are not the starting points of any snake or ladder.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class Solution:

        def snakes_and_ladders(self, board: list[list[int]]) -> int:
            raise NotImplementedError('Implement snakes_and_ladders')

    practice_exports = {'deque': deque, 'Solution': Solution}
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
