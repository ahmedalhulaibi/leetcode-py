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
    # 651. 4 Keys Keyboard

    **Medium** · Math, Dynamic Programming

    Imagine you have a special keyboard with the following keys:

    - `A`: Print one `'A'` on the screen.
    - `Ctrl-A`: Select the whole screen.
    - `Ctrl-C`: Copy selection to buffer.
    - `Ctrl-V`: Print buffer on screen appending it after what has already been printed.

    Given an integer `n`, return *the maximum number of* `'A'` *you can print on the screen with at most* `n` *presses on the keys*.

    ## Examples

    ```
    Input: n = 3
    Output: 3
    Explanation: We can at most get 3 A's on screen by pressing the following key sequence: A, A, A
    ```

    ```
    Input: n = 7
    Output: 9
    Explanation: We can at most get 9 A's on screen by pressing the following key sequence: A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
    ```

    ## Constraints

    - `1 <= n <= 50`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_a(self, n: int) -> int:
            raise NotImplementedError('Implement max_a')

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
