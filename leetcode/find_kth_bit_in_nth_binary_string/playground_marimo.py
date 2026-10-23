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
    # 1545. Find Kth Bit in Nth Binary String

    **Medium** · String, Recursion, Simulation

    Given two positive integers `n` and `k`, the binary string `S_n` is formed as follows:

    - `S_1 = "0"`
    - `S_i = S_i - 1 + "1" + reverse(invert(S_i - 1))` for `i > 1`

    Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1` changes to `0`).

    For example, the first four strings in the above sequence are:

    - `S_1 = "0"`
    - `S_2 = "011"`
    - `S_3 = "0111001"`
    - `S_4 = "011100110110001"`

    Return *the* `k^th` *bit* *in* `S_n`. It is guaranteed that `k` is valid for the given `n`.

    ## Examples

    ```
    Input: n = 3, k = 1
    Output: "0"
    Explanation: S3 is "0111001".
    The 1st bit is "0".
    ```

    ```
    Input: n = 4, k = 11
    Output: "1"
    Explanation: S4 is "011100110110001".
    The 11th bit is "1".
    ```

    ## Constraints

    - `1 <= n <= 20`
    - `1 <= k <= 2^n - 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_kth_bit(self, n: int, k: int) -> str:
            raise NotImplementedError('Implement find_kth_bit')

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
