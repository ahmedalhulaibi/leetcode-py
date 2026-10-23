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
    # 679. 24 Game

    **Hard** · Array, Math, Backtracking

    You are given an integer array `cards` of length `4`. You have four cards, each containing a number in the range `[1, 9]`. You should arrange the numbers on these cards in a mathematical expression using the operators `['+', '-', '*', '/']` and the parentheses `'('` and `')'` to get the value 24.

    You are restricted with the following rules:

    - The division operator `'/'` represents real division, not integer division.
        - For example, `4 / (1 - 2 / 3) = 4 / (1 / 3) = 12`.
    - Every operation done is between two numbers. In particular, we cannot use `'-'` as a unary operator.
        - For example, if `cards = [1, 1, 1, 1]`, the expression `"-1 - 1 - 1 - 1"` is **not allowed**.
    - You cannot concatenate numbers together
        - For example, if `cards = [1, 2, 1, 2]`, the expression `"12 + 12"` is not valid.

    Return `true` if you can get such expression that evaluates to 24, and `false` otherwise.

    ## Examples

    ```
    Input: cards = [4,1,8,7]
    Output: true
    Explanation: (8-4) * (7-1) = 24
    ```

    ```
    Input: cards = [1,2,1,2]
    Output: false
    ```

    ## Constraints

    - cards.length == 4
    - 1 <= cards[i] <= 9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def judge_point24(self, cards: list[int]) -> bool:
            raise NotImplementedError('Implement judge_point24')

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
