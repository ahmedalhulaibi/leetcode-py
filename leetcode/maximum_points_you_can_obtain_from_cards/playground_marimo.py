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
    # 1423. Maximum Points You Can Obtain from Cards

    **Medium** · Array, Sliding Window, Prefix Sum

    There are several cards <strong>arranged in a row</strong>, and each card has an associated number of points. The points are given in the integer array <code>cardPoints</code>.

    In one step, you can take one card from the beginning or from the end of the row. You have to take exactly <code>k</code> cards.

    Your score is the sum of the points of the cards you have taken.

    Given the integer array <code>cardPoints</code> and the integer <code>k</code>, return the <em>maximum score</em> you can obtain.

    ## Examples

    ```
    Input: cardPoints = [1,2,3,4,5,6,1], k = 3
    Output: 12
    ```
    **Explanation:** After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

    ```
    Input: cardPoints = [2,2,2], k = 2
    Output: 4
    ```
    **Explanation:** Regardless of which two cards you take, your score will always be 4.

    ```
    Input: cardPoints = [9,7,7,9,7,7,9], k = 7
    Output: 55
    ```
    **Explanation:** You have to take all the cards. Your score is the sum of points of all cards.

    ## Constraints

    - `1 <= cardPoints.length <= 10^5`
    - `1 <= cardPoints[i] <= 10^4`
    - `1 <= k <= cardPoints.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_score(self, card_points: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_score')

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
