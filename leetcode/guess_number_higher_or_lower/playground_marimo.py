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
    # 374. Guess Number Higher or Lower

    **Easy** · Binary Search, Interactive

    We are playing the Guess Game. The game is as follows:

    I pick a number from `1` to `n`. You have to guess which number I picked. Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

    You call a pre-defined API `int guess(int num)`, which returns three possible results:

    - `-1`: Your guess is higher than the number I picked (i.e. `num > pick`).
    - `1`: Your guess is lower than the number I picked (i.e. `num < pick`).
    - `0`: your guess is equal to the number I picked (i.e. `num == pick`).

    Return *the number that I picked*.

    ## Examples

    ```
    Input: n = 10, pick = 6
    Output: 6
    ```

    ```
    Input: n = 1, pick = 1
    Output: 1
    ```

    ```
    Input: n = 2, pick = 1
    Output: 1
    ```

    ## Constraints

    - 1 <= n <= 2^31 - 1
    - 1 <= pick <= n



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    def guess(num: int) -> int:
        raise NotImplementedError

    class Solution:

        def guess_number(self, n: int) -> int:
            raise NotImplementedError('Implement guess_number')

    practice_exports = {'guess': guess, 'Solution': Solution}
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
