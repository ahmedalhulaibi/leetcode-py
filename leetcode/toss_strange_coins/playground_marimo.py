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
    # 1230. Toss Strange Coins

    **Medium** · Array, Math, Dynamic Programming, Probability and Statistics

    You have some coins. The `i`-th coin has a probability `prob[i]` of facing heads when tossed.

    Return the probability that the number of coins facing heads equals `target` if you toss every coin exactly once.

    ## Examples

    ```
    Input: prob = [0.4], target = 1
    Output: 0.40000
    ```

    ```
    Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
    Output: 0.03125
    ```

    ## Constraints

    - 1 <= prob.length <= 1000
    - 0 <= prob[i] <= 1
    - 0 <= target <= prob.length
    - Answers will be accepted as correct if they are within `10^-5` of the correct answer.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def probability_of_heads(self, prob: list[float], target: int) -> float:
            raise NotImplementedError('Implement probability_of_heads')

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
