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
    # 544. Output Contest Matches

    **Medium** · Recursion, String, Simulation

    During the NBA playoffs, we always set the rather strong team to play with the rather weak team, like making the rank `1` team play with the rank `n`th team, which is a good strategy to make the contest more interesting.

    Given `n` teams, return their final contest matches in the form of a string.

    The `n` teams are labeled from `1` to `n`, which represents their initial rank (i.e., Rank `1` is the strongest team and Rank `n` is the weakest team).

    We will use parentheses `'('`, and `')'` and commas `','` to represent the contest team pairing. We use the parentheses for pairing and the commas for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.

    ## Examples

    ```
    Input: n = 4
    Output: "((1,4),(2,3))"
    Explanation:
    In the first round, we pair the team 1 and 4, the teams 2 and 3 together, as we need to make the strong team and weak team together.
    And we got (1, 4),(2, 3).
    In the second round, the winners of (1, 4) and (2, 3) need to play again to generate the final winner, so you need to add the parentheses outside them.
    And we got the final answer ((1,4),(2,3)).
    ```

    ```
    Input: n = 8
    Output: "(((1,8),(4,5)),((2,7),(3,6)))"
    Explanation:
    First round: (1, 8),(2, 7),(3, 6),(4, 5)
    Second round: ((1, 8),(4, 5)),((2, 7),(3, 6))
    Third round: (((1, 8),(4, 5)),((2, 7),(3, 6)))
    Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
    ```

    ## Constraints

    - `n == 2^x` where `x` is in the range `[1, 12]`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_contest_match(self, n: int) -> str:
            raise NotImplementedError('Implement find_contest_match')

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
