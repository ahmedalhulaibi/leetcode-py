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
    # 2429. Minimize XOR

    **Medium** · Greedy, Bit Manipulation

    Given two positive integers `num1` and `num2`, find the positive integer `x` such that:

    - `x` has the same number of set bits as `num2`, and
    - The value `x XOR num1` is **minimal**.

    Note that XOR is the bitwise XOR operation.

    Return the integer `x`. The test cases are generated such that `x` is uniquely determined.

    The number of set bits of an integer is the number of `1`'s in its binary representation.

    ## Examples

    ```
    Input: num1 = 3, num2 = 5
    Output: 3
    Explanation:
    The binary representations of num1 and num2 are 0011 and 0101, respectively.
    The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
    ```

    ```
    Input: num1 = 1, num2 = 12
    Output: 3
    Explanation:
    The binary representations of num1 and num2 are 0001 and 1100, respectively.
    The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
    ```

    ## Constraints

    - 1 <= num1, num2 <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimize_xor(self, num1: int, num2: int) -> int:
            raise NotImplementedError('Implement minimize_xor')

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
