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
    # 294. Flip Game II

    **Medium** · Memoization, Math, Dynamic Programming, Backtracking, Game Theory

    You are playing a Flip Game with your friend.

    You are given a string `currentState` that contains only `'+'` and `'-'`. You and your friend take turns to flip **two consecutive** `"++"` into `"--"`. The game ends when a person can no longer make a move, and therefore the other person will be the winner.

    Return `true` *if the starting player can **guarantee a win***, and `false` otherwise.

    **Follow up:** Derive your algorithm's runtime complexity.

    ## Examples

    ```
    Input: currentState = "++++"
    Output: true
    Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
    ```

    ```
    Input: currentState = "+"
    Output: false
    ```

    ## Constraints

    - `1 <= currentState.length <= 60`
    - `currentState[i]` is either `'+'` or `'-'`.
    - There cannot be more than 20 consecutive `'+'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_win(self, current_state: str) -> bool:
            raise NotImplementedError('Implement can_win')

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
