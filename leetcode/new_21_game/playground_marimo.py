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
    # 837. New 21 Game

    **Medium** · Math, Dynamic Programming, Sliding Window, Probability and Statistics

    Alice plays the following game, loosely based on the card game `"21"`.

    Alice starts with `0` points and draws numbers while she has less than `k` points. During each draw, she gains an integer number of points randomly from the range `[1, maxPts]`, where `maxPts` is an integer. Each draw is independent and the outcomes have equal probabilities.

    Alice stops drawing numbers when she gets `k` or more points.

    Return the probability that Alice has `n` or fewer points.

    Answers within `10-5` of the actual answer are considered accepted.

    ## Examples

    ```
    Input: n = 10, k = 1, maxPts = 10
    Output: 1.00000
    Explanation: Alice gets a single card, then stops.
    ```

    ```
    Input: n = 6, k = 1, maxPts = 10
    Output: 0.60000
    Explanation: Alice gets a single card, then stops.
    In 6 out of 10 possibilities, she is at or below 6 points.
    ```

    ```
    Input: n = 21, k = 17, maxPts = 10
    Output: 0.73278
    ```

    ## Constraints

    - 0 <= k <= n <= 10^4
    - 1 <= maxPts <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def new21_game(self, n: int, k: int, max_pts: int) -> float:
            raise NotImplementedError('Implement new21_game')

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
