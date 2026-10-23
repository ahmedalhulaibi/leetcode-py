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
    # 499. The Maze III

    **Hard** · Depth-First Search, Breadth-First Search, Graph, Array, String, Matrix, Shortest Path, Dijkstra, Heap (Priority Queue)

    There is a ball in a `maze` with empty spaces (represented as `0`) and walls (represented as `1`). The ball can go through the empty spaces by rolling **up, down, left or right**, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction (must be different from last chosen direction). There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.

    Given the `m x n` `maze`, the ball's position `ball` and the hole's position `hole`, where `ball = [ball_row, ball_col]` and `hole = [hole_row, hole_col]`, return a string `instructions` of all the instructions that the ball should follow to drop in the hole with the **shortest distance** possible. If there are multiple valid instructions, return the **lexicographically minimum** one. If the ball can't drop in the hole, return `"impossible"`.

    If there is a way for the ball to drop in the hole, the answer `instructions` should contain the characters `'u'` (i.e. up), `'d'` (i.e. down), `'l'` (i.e. left), and `'r'` (i.e. right).

    The **distance** is the number of **empty spaces** traveled by the ball from the start position (excluded) to the destination (included).

    You may assume that **the borders of the maze are all walls** (see examples).

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0499.The%20Maze%20III/images/maze3-1-grid.jpg)

    ```
    Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [0,1]
    Output: "lul"
    Explanation: There are two shortest ways for the ball to drop into the hole. The first way is left -> up -> left, represented by "lul". The second way is up -> left, represented by 'ul'. Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0499.The%20Maze%20III/images/maze3-2-grid.jpg)

    ```
    Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [3,0]
    Output: "impossible"
    Explanation: The ball cannot reach the hole.
    ```

    ```
    Input: maze = [[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]], ball = [0,4], hole = [3,5]
    Output: "dldr"
    ```

    ## Constraints

    - `m == maze.length`
    - `n == maze[i].length`
    - `1 <= m, n <= 100`
    - `maze[i][j]` is `0` or `1`.
    - `ball.length == 2`
    - `hole.length == 2`
    - `0 <= ball_row, hole_row <= m`
    - `0 <= ball_col, hole_col <= n`
    - Both the ball and the hole exist in an empty space, and they will not be in the same position initially.
    - The maze contains **at least 2 empty spaces**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_shortest_way(self, maze: list[list[int]], ball: list[int], hole: list[int]) -> str:
            raise NotImplementedError('Implement find_shortest_way')

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
