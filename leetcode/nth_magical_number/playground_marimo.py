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
    # 878. Nth Magical Number

    **Hard** · Math, Binary Search, Number Theory

    A positive integer is magical if it is divisible by either `a` or `b`.

    Given the three integers `n`, `a`, and `b`, return the nth magical number. Since the answer may be very large, return it modulo `10^9 + 7`.

    ## Examples

    ```
    Input: n = 1, a = 2, b = 3
    Output: 2
    ```

    ```
    Input: n = 4, a = 2, b = 3
    Output: 6
    ```

    ## Constraints

    - 1 <= n <= 10^9
    - 2 <= a, b <= 4 * 10^4

    **Follow up:** Could you solve the problem in `O(log(n * min(a, b)))` time complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def nth_magical_number(self, n: int, a: int, b: int) -> int:
            raise NotImplementedError('Implement nth_magical_number')

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
