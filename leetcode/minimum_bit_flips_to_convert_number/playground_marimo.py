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
    # 2220. Minimum Bit Flips to Convert Number

    **Easy** · Bit Manipulation

    A **bit flip** of a number `x` is choosing a bit in the binary representation of `x` and **flipping** it from either `0` to `1` or `1` to `0`.

    - For example, for `x = 7`, the binary representation is `111` and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get `110`, flip the second bit from the right to get `101`, flip the fifth bit from the right (a leading zero) to get `10111`, etc.

    Given two integers `start` and `goal`, return *the **minimum** number of **bit flips** to convert* `start` *to* `goal`.

    ## Examples

    ```
    Input: start = 10, goal = 7
    Output: 3
    Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
    - Flip the first bit from the right: 1010 -> 1011.
    - Flip the third bit from the right: 1011 -> 1111.
    - Flip the fourth bit from the right: 1111 -> 0111.
    It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
    ```

    ```
    Input: start = 3, goal = 4
    Output: 3
    Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
    - Flip the first bit from the right: 011 -> 010.
    - Flip the second bit from the right: 010 -> 000.
    - Flip the third bit from the right: 000 -> 100.
    It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.
    ```

    ## Constraints

    - 0 <= start, goal <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_bit_flips(self, start: int, goal: int) -> int:
            raise NotImplementedError('Implement min_bit_flips')

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
