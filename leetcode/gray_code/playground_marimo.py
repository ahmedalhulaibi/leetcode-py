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
    # 89. Gray Code

    **Medium** · Math, Backtracking, Bit Manipulation

    An **n-bit gray code sequence** is a sequence of `2^n` integers where:

    - Every integer is in the **inclusive** range `[0, 2^n - 1]`,
    - The first integer is `0`,
    - An integer appears **no more than once** in the sequence,
    - The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and
    - The binary representation of the **first** and **last** integers differs by **exactly one bit**.

    Given an integer `n`, return *any valid* **n-bit gray code sequence**.

    ## Examples

    ```
    Input: n = 2
    Output: [0,1,3,2]
    Explanation: The binary representation of [0,1,3,2] is [00,01,11,10].
    - 00 and 01 differ by one bit
    - 01 and 11 differ by one bit
    - 11 and 10 differ by one bit
    - 10 and 00 differ by one bit
    [0,2,3,1] is also a valid gray code sequence.
    ```

    ```
    Input: n = 1
    Output: [0,1]
    ```

    ## Constraints

    - `1 <= n <= 16`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def gray_code(self, n: int) -> list[int]:
            raise NotImplementedError('Implement gray_code')

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
