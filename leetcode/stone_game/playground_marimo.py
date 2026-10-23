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
    # 877. Stone Game

    **Medium** · Array, Math, Dynamic Programming, Game Theory

    Alice and Bob play a game with piles of stones. There are an **even** number of piles arranged in a row, and each pile has a **positive** integer number of stones `piles[i]`.

    The objective of the game is to end with the most stones. The **total** number of stones across all the piles is **odd**, so there are no ties.

    Alice and Bob take turns, with **Alice starting first**. Each turn, a player takes the entire pile of stones either from the **beginning** or from the **end** of the row. This continues until there are no more piles left, at which point the person with the **most stones wins**.

    Assuming Alice and Bob play optimally, return `true` if Alice wins the game, or `false` if Bob wins.

    ## Examples

    ```
    Input: piles = [5,3,4,5]
    Output: true
    Explanation:
    Alice starts first, and can only take the first 5 or the last 5.
    Say she takes the first 5, so that the row becomes [3, 4, 5].
    If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
    If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
    This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
    ```

    ```
    Input: piles = [3,7,2,3]
    Output: true
    ```

    ## Constraints

    - 2 <= piles.length <= 500
    - `piles.length` is even.
    - 1 <= piles[i] <= 500
    - `sum(piles[i])` is odd.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def stone_game(self, piles: list[int]) -> bool:
            raise NotImplementedError('Implement stone_game')

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
