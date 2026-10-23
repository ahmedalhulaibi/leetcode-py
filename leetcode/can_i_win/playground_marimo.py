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
    # 464. Can I Win

    **Medium** · Math, Dynamic Programming, Bit Manipulation, Memoization, Game Theory, Bitmask

    In the "100 game" two players take turns adding, to a running total, any integer from `1` to `10`. The player who first causes the running total to **reach or exceed** 100 wins.

    What if we change the game so that players **cannot** re-use integers?

    For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

    Given two integers `maxChoosableInteger` and `desiredTotal`, return `true` if the first player to move can force a win, otherwise, return `false`. Assume both players play optimally.

    ## Examples

    ```
    Input: maxChoosableInteger = 10, desiredTotal = 11
    Output: false
    Explanation:
    No matter which integer the first player choose, the first player will lose.
    The first player can choose an integer from 1 up to 10.
    If the first player choose 1, the second player can only choose integers from 2 up to 10.
    The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
    Same with other integers chosen by the first player, the second player will always win.
    ```

    ```
    Input: maxChoosableInteger = 10, desiredTotal = 0
    Output: true
    ```

    ```
    Input: maxChoosableInteger = 10, desiredTotal = 1
    Output: true
    ```

    ## Constraints

    - 1 <= maxChoosableInteger <= 20
    - 0 <= desiredTotal <= 300



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_i_win(self, max_choosable_integer: int, desired_total: int) -> bool:
            raise NotImplementedError('Implement can_i_win')

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
