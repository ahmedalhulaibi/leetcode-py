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
    # 1611. Minimum One Bit Operations to Make Integers Zero

    **Hard** · Math, Dynamic Programming, Bit Manipulation, Recursion, Memoization

    Given an integer `n`, you must transform it into `0` using the following operations any number of times:

    - Change the rightmost (0th) bit in the binary representation of `n`.
    - Change the `ith` bit in the binary representation of `n` if the `(i-1)th` bit is set to `1` and the `(i-2)th` through `0th` bits are set to `0`.

    Return the minimum number of operations to transform `n` into `0`.

    ## Examples

    ```
    Input: n = 3
    Output: 2
    Explanation: The binary representation of 3 is "11".
    "11" -> "01" with the 2nd operation since the 0th bit is 1.
    "01" -> "00" with the 1st operation.
    ```

    ```
    Input: n = 6
    Output: 4
    Explanation: The binary representation of 6 is "110".
    "110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
    "010" -> "011" with the 1st operation.
    "011" -> "001" with the 2nd operation since the 0th bit is 1.
    "001" -> "000" with the 1st operation.
    ```

    ## Constraints

    - 0 <= n <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_one_bit_operations(self, n: int) -> int:
            raise NotImplementedError('Implement minimum_one_bit_operations')

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
