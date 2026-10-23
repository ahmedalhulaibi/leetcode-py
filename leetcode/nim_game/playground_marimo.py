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
    # 292. Nim Game

    **Easy** · Math, Brainteaser, Game Theory

    You are playing the following Nim Game with your friend:

    - Initially, there is a heap of stones on the table.
    - You and your friend will alternate taking turns, and **you go first**.
    - On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
    - The one who removes the last stone is the winner.

    Given `n`, the number of stones in the heap, return `true` if you can win the game assuming both you and your friend play optimally, otherwise return `false`.

    ## Examples

    ```
    Input: n = 4
    Output: false
    Explanation: These are the possible outcomes:
    1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
    2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
    3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
    In all outcomes, your friend wins.
    ```

    ```
    Input: n = 1
    Output: true
    ```

    ```
    Input: n = 2
    Output: true
    ```

    ## Constraints

    - 1 <= n <= 2^31 - 1

    **Follow up:** Could you solve it with a closed-form solution instead of a DP?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_win_nim(self, n: int) -> bool:
            raise NotImplementedError('Implement can_win_nim')

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
