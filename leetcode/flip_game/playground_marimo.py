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
    # 293. Flip Game

    **Easy** · String

    You are playing a Flip Game with your friend.

    You are given a string `currentState` that contains only `'+'` and `'-'`. You and your friend take turns to flip **two consecutive** `"++"` into `"--"`. The game ends when a person can no longer make a move, and therefore the other person will be the winner.

    Return all possible states of the string `currentState` after **one valid move**. You may return the answer in **any order**. If there is no valid move, return an empty list `[]`.

    ## Examples

    ```
    Input: currentState = "++++"
    Output: ["--++","+--+","++--"]
    ```

    ```
    Input: currentState = "+"
    Output: []
    ```

    ## Constraints

    - `1 <= currentState.length <= 500`
    - `currentState[i]` is either `'+'` or `'-'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def generate_possible_next_moves(self, current_state: str) -> list[str]:
            raise NotImplementedError('Implement generate_possible_next_moves')

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
