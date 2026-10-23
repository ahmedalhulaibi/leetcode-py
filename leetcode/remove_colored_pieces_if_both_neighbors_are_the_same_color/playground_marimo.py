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
    # 2038. Remove Colored Pieces if Both Neighbors are the Same Color

    **Medium** · Math, String, Greedy, Game Theory

    There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

    Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.


        Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
        Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
        Alice and Bob cannot remove pieces from the edge of the line.
        If a player cannot make a move on their turn, that player loses and the other player wins.


    Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

    ## Examples

    ```
    Input: colors = "AAABABB"
    Output: true
    Explanation: AA<u>A</u>BABB -> AABABB
    Alice moves first.
    She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

    Now it's Bob's turn.
    Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
    Thus, Alice wins, so return true.
    ```

    ```
    Input: colors = "AA"
    Output: false
    Explanation: Alice has her turn first.
    There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
    Thus, Bob wins, so return false.
    ```

    ```
    Input: colors = "ABBBBBBBAAA"
    Output: false
    Explanation: ABBBBBBBA<u>A</u>A -> ABBBBBBBAA
    Alice moves first.
    Her only option is to remove the second to last 'A' from the right.

    ABBBB<u>B</u>BBAA -> ABBBBBBAA
    Next is Bob's turn.
    He has many options for which 'B' piece to remove. He can pick any.

    On Alice's second turn, she has no more pieces that she can remove.
    Thus, Bob wins, so return false.
    ```

    ## Constraints

    - 1 <= colors.length <= 10^5
    - colors consists of only the letters 'A' and 'B'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def winner_of_game(self, colors: str) -> bool:
            raise NotImplementedError('Implement winner_of_game')

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
