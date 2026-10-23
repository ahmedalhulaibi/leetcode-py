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
    # 842. Split Array into Fibonacci Sequence

    **Medium** · String, Backtracking

    You are given a string of digits `num`, such as `"123456579"`. We can split it into a Fibonacci-like sequence `[123, 456, 579]`.

    Formally, a **Fibonacci-like** sequence is a list `f` of non-negative integers such that:

    - `0 <= f[i] < 2^31`, (that is, each integer fits in a **32-bit** signed integer type),
    - `f.length >= 3`, and
    - `f[i] + f[i + 1] == f[i + 2]` for all `0 <= i < f.length - 2`.

    Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number `0` itself.

    Return any Fibonacci-like sequence split from `num`, or return `[]` if it cannot be done.

    ## Examples

    ```
    Input: num = "1101111"
    Output: [11,0,11,11]
    Explanation: The output [110, 1, 111] would also be accepted.
    ```

    ```
    Input: num = "112358130"
    Output: []
    Explanation: The task is impossible.
    ```

    ```
    Input: num = "0123"
    Output: []
    Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
    ```

    ## Constraints

    - `1 <= num.length <= 200`
    - `num` contains only digits.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def split_into_fibonacci(self, num: str) -> list[int]:
            raise NotImplementedError('Implement split_into_fibonacci')

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
