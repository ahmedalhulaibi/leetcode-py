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
    # 397. Integer Replacement

    **Medium** · Dynamic Programming, Greedy, Bit Manipulation, Memoization

    Given a positive integer `n`, you can apply one of the following operations:

    - If `n` is even, replace `n` with `n / 2`.
    - If `n` is odd, replace `n` with either `n + 1` or `n - 1`.

    Return the minimum number of operations needed for `n` to become `1`.

    ## Examples

    ```
    Input: n = 8
    Output: 3
    Explanation: 8 -> 4 -> 2 -> 1
    ```

    ```
    Input: n = 7
    Output: 4
    Explanation: 7 -> 8 -> 4 -> 2 -> 1
    or 7 -> 6 -> 3 -> 2 -> 1
    ```

    ```
    Input: n = 4
    Output: 2
    ```

    ## Constraints

    - 1 <= n <= 2^31 - 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def integer_replacement(self, n: int) -> int:
            raise NotImplementedError('Implement integer_replacement')

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
