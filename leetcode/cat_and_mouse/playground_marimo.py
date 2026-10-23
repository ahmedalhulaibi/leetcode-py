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
    # 913. Cat and Mouse

    **Hard** · Math, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Minimax, Game Theory, Zero-Sum Game

    A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

    The graph is given as follows: `graph[a]` is a list of all nodes `b` such that `ab` is an edge of the graph.

    The mouse starts at node `1` and goes first, the cat starts at node `2` and goes second, and there is a hole at node `0`.

    During each player's turn, they must travel along one edge of the graph that meets where they are. For example, if the Mouse is at node 1, it must travel to any node in `graph[1]`.

    Additionally, it is not allowed for the Cat to travel to the Hole (node `0`).

    Then, the game can end in three ways:

    - If ever the Cat occupies the same node as the Mouse, the Cat wins.
    - If ever the Mouse reaches the Hole, the Mouse wins.
    - If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.

    Given a `graph`, and assuming both players play optimally, return

    - `1` if the mouse wins the game,
    - `2` if the cat wins the game, or
    - `0` if the game is a draw.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/11/17/cat1.jpg)

    ```
    Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    Output: 0
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/11/17/cat2.jpg)

    ```
    Input: graph = [[1,3],[0],[3],[0,2]]
    Output: 1
    ```

    ## Constraints

    - 3 <= graph.length <= 50
    - 1 <= graph[i].length < graph.length
    - 0 <= graph[i][j] < graph.length
    - graph[i][j] != i
    - graph[i] is unique.
    - The mouse and the cat can always move.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def cat_mouse_game(self, graph: list[list[int]]) -> int:
            raise NotImplementedError('Implement cat_mouse_game')

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
