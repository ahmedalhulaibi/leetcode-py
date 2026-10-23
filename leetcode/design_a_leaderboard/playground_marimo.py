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
    # 1244. Design A Leaderboard

    **Medium** · Design, Hash Table, Sorting

    Design a Leaderboard class, which has 3 functions:

    - `addScore(playerId, score)`: Update the leaderboard by adding `score` to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given `score`.
    - `top(K)`: Return the score sum of the top `K` players.
    - `reset(playerId)`: Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

    Initially, the leaderboard is empty.

    ## Examples

    ```
    Input:
    ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
    [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
    Output:
    [null,null,null,null,null,null,73,null,null,null,141]

    Explanation
    Leaderboard leaderboard = new Leaderboard();
    leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
    leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
    leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
    leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
    leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
    leaderboard.top(1);           // returns 73;
    leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
    leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
    leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
    leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
    ```

    ## Constraints

    - `1 <= playerId, K <= 10^4`
    - It's guaranteed that `K` is less than or equal to the current number of players.
    - `1 <= score <= 100`
    - At most `1000` function calls will be made.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Leaderboard:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def add_score(self, player_id: int, score: int) -> None:
            raise NotImplementedError('Implement add_score')

        def top(self, k: int) -> int:
            raise NotImplementedError('Implement top')

        def reset(self, player_id: int) -> None:
            raise NotImplementedError('Implement reset')

    practice_exports = {'Leaderboard': Leaderboard}
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
