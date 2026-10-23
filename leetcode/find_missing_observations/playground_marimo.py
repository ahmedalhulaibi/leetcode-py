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
    # 2028. Find Missing Observations

    **Medium** · Array, Math, Simulation

    You have observations of `n + m` **6-sided** dice rolls with each face numbered from `1` to `6`. `n` of the observations went missing, and you only have the observations of `m` rolls. Fortunately, you have also calculated the **average value** of the `n + m` rolls.

    You are given an integer array `rolls` of length `m` where `rolls[i]` is the value of the `i`th observation. You are also given the two integers `mean` and `n`.

    Return an array of length `n` containing the missing observations such that the **average value** of the `n + m` rolls is **exactly** `mean`. If there are multiple valid answers, return **any of them**. If no such array exists, return an empty array.

    The **average value** of a set of `k` numbers is the sum of the numbers divided by `k`.

    Note that `mean` is an integer, so the sum of the `n + m` rolls should be divisible by `n + m`.

    ## Examples

    ```
    Input: rolls = [3,2,4,3], mean = 4, n = 2
    Output: [6,6]
    Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
    ```

    ```
    Input: rolls = [1,5,6], mean = 3, n = 4
    Output: [2,3,2,2]
    Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
    ```

    ```
    Input: rolls = [1,2,3,4], mean = 6, n = 4
    Output: []
    Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
    ```

    ## Constraints

    - `m == rolls.length`
    - `1 <= n, m <= 10^5`
    - `1 <= rolls[i], mean <= 6`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def missing_rolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
            raise NotImplementedError('Implement missing_rolls')

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
