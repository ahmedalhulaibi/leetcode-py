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
    # 822. Card Flipping Game

    **Medium** · Array, Hash Table

    You are given two <strong>0-indexed</strong> integer arrays <code>fronts</code> and <code>backs</code> of length <code>n</code>, where the <code>i<sup>th</sup></code> card has the positive integer <code>fronts[i]</code> printed on the front and <code>backs[i]</code> printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).

    After flipping the cards, an integer is considered <strong>good</strong> if it is facing down on some card and <strong>not</strong> facing up on any card.

    Return <em>the minimum possible good integer after flipping the cards</em>. If there are no good integers, return <code>0</code>.

    ## Examples

    ```
    Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
    Output: 2
    Explanation:
    If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3].
    2 is the minimum good integer as it appears facing down but not facing up.
    It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.
    ```

    ```
    Input: fronts = [1], backs = [1]
    Output: 0
    Explanation:
    There are no good integers no matter how we flip the cards, so we return 0.
    ```

    ## Constraints

    - n == fronts.length == backs.length
    - 1 <= n <= 1000
    - 1 <= fronts[i], backs[i] <= 2000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def flipgame(self, fronts: list[int], backs: list[int]) -> int:
            raise NotImplementedError('Implement flipgame')

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
