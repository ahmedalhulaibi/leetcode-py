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
    # 808. Soup Servings

    **Medium** · Math, Dynamic Programming, Probability and Statistics

    You have two soups, A and B, each starting with `n` mL. On every turn, one of the following four serving operations is chosen at random, each with probability `0.25` independent of all previous turns:

    - pour 100 mL from type A and 0 mL from type B
    - pour 75 mL from type A and 25 mL from type B
    - pour 50 mL from type A and 50 mL from type B
    - pour 25 mL from type A and 75 mL from type B

    Note:

    - There is no operation that pours 0 mL from A and 100 mL from B.
    - The amounts from A and B are poured simultaneously during the turn.
    - If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.

    The process stops immediately after any turn in which one of the soups is used up.

    Return the probability that A is used up before B, plus half the probability that both soups are used up in the same turn. Answers within 10^-5 of the actual answer will be accepted.

    ## Examples

    ```
    Input: n = 50
    Output: 0.62500
    Explanation:
    If we perform either of the first two serving operations, soup A will become empty first.
    If we perform the third operation, A and B will become empty at the same time.
    If we perform the fourth operation, B will become empty first.
    So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
    ```

    ```
    Input: n = 100
    Output: 0.71875
    Explanation:
    If we perform the first serving operation, soup A will become empty first.
    If we perform the second serving operations, A will become empty on performing operation [1, 2, 3], and both A and B become empty on performing operation 4.
    If we perform the third operation, A will become empty on performing operation [1, 2], and both A and B become empty on performing operation 3.
    If we perform the fourth operation, A will become empty on performing operation 1, and both A and B become empty on performing operation 2.
    So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.71875.
    ```

    ## Constraints

    - 0 <= n <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from functools import cache

    class Solution:

        def soup_servings(self, n: int) -> float:
            raise NotImplementedError('Implement soup_servings')

    practice_exports = {'cache': cache, 'Solution': Solution}
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
