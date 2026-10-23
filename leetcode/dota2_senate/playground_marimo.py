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
    # 649. Dota2 Senate

    **Medium** · String, Greedy, Queue

    In the world of Dota2, there are two parties: the Radiant and the Dire.

    The Dota2 senate consists of senators from both parties. Voting is a round-based procedure. In each round, each senator (in order) can exercise one right:

    - **Ban one senator's right:** make another senator lose all rights in this and all following rounds.
    - **Announce the victory:** if all senators who still have rights are from the same party, announce victory.

    Given a string `senate` where `'R'` is Radiant and `'D'` is Dire, predict which party announces victory. Output `"Radiant"` or `"Dire"`. Every senator plays optimally for their own party.

    ## Examples

    ```
    Input: senate = "RD"
    Output: "Radiant"
    Explanation: The first senator (Radiant) bans the next senator's right in round 1. In round 2, the first senator announces victory.
    ```

    ```
    Input: senate = "RDD"
    Output: "Dire"
    Explanation: The first senator (Radiant) bans the second senator's right. The third senator (Dire) bans the first senator's right. In round 2, the third senator announces victory.
    ```

    ## Constraints

    - n == senate.length
    - 1 <= n <= 10^4
    - senate[i] is either 'R' or 'D'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class Solution:

        def predict_party_victory(self, senate: str) -> str:
            raise NotImplementedError('Implement predict_party_victory')

    practice_exports = {'deque': deque, 'Solution': Solution}
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
