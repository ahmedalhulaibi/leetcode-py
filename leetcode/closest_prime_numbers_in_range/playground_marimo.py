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
    # 2523. Closest Prime Numbers in Range

    **Medium** · Math, Number Theory, Primality Test, Sieve Theory, Prime Number Sieve

    Given two positive integers `left` and `right`, find the two integers `num1` and `num2` such that:

    - `left <= num1 < num2 <= right`.
    - Both `num1` and `num2` are prime numbers.
    - `num2 - num1` is the **minimum** amongst all other pairs satisfying the above conditions.

    Return the positive integer array `ans = [num1, num2]`. If there are multiple pairs satisfying these conditions, return the one with the **smallest** `num1` value. If no such numbers exist, return `[-1, -1]`.

    ## Examples

    ```
    Input: left = 10, right = 19
    Output: [11,13]
    Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
    The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
    Since 11 is smaller than 17, we return the first pair.
    ```

    ```
    Input: left = 4, right = 6
    Output: [-1,-1]
    Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
    ```

    ## Constraints

    - 1 <= left <= right <= 10<sup>6</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def closest_primes(self, left: int, right: int) -> list[int]:
            raise NotImplementedError('Implement closest_primes')

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
