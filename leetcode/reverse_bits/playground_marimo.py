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
    # 190. Reverse Bits

    **Easy** · Divide and Conquer, Bit Manipulation

    Reverse bits of a given 32 bits signed integer.

    ## Examples

    ```
    Input: n = 43261596
    Output: 964176192
    Explanation:

    | Integer    | Binary                              |
    |------------|-------------------------------------|
    | 43261596   | 00000010100101000001111010011100    |
    | 964176192  | 00111001011110000010100101000000    |
    ```

    ```
    Input: n = 2147483644
    Output: 1073741822
    Explanation:

    | Integer     | Binary                              |
    |-------------|-------------------------------------|
    | 2147483644  | 01111111111111111111111111111100    |
    | 1073741822  | 00111111111111111111111111111110    |
    ```

    ## Constraints

    - 0 <= n <= 2^31 - 2
    - n is even.

    **Follow up:** If this function is called many times, how would you optimize it?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def reverse_bits(self, n: int) -> int:
            raise NotImplementedError('Implement reverse_bits')

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
