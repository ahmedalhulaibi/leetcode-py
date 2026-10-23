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
    # 1688. Count of Matches in Tournament

    **Easy** · Math, Simulation

    You are given an integer `n`, the number of teams in a tournament that has strange rules:

    - If the current number of teams is **even**, each team gets paired with another team. A total of `n / 2` matches are played, and `n / 2` teams advance to the next round.
    - If the current number of teams is **odd**, one team randomly advances in the tournament, and the rest gets paired. A total of `(n - 1) / 2` matches are played, and `(n - 1) / 2 + 1` teams advance to the next round.

    Return *the number of matches played in the tournament until a winner is decided.*

    ## Examples

    ```
    Input: n = 7
    Output: 6
    Explanation: Details of the tournament:
    - 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
    - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
    - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
    Total number of matches = 3 + 2 + 1 = 6.
    ```

    ```
    Input: n = 14
    Output: 13
    Explanation: Details of the tournament:
    - 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
    - 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
    - 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
    - 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
    Total number of matches = 7 + 3 + 2 + 1 = 13.
    ```

    ## Constraints

    - `1 <= n <= 200`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def number_of_matches(self, n: int) -> int:
            raise NotImplementedError('Implement number_of_matches')

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
