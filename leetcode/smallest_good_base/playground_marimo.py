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
    # 483. Smallest Good Base

    **Hard** · Math, Binary Search

    Given an integer `n` represented as a string, return *the smallest **good base** of* `n`.

    We call `k >= 2` a **good base** of `n`, if all digits of `n` base `k` are `1`'s.

    ## Examples

    ```
    Input: n = "13"
    Output: "3"
    Explanation: 13 base 3 is 111.
    ```

    ```
    Input: n = "4681"
    Output: "8"
    Explanation: 4681 base 8 is 11111.
    ```

    ```
    Input: n = "1000000000000000000"
    Output: "999999999999999999"
    Explanation: 1000000000000000000 base 999999999999999999 is 11.
    ```

    ## Constraints

    - n is an integer in the range [3, 10^18]
    - n does not contain any leading zeros.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def smallest_good_base(self, n: str) -> str:
            raise NotImplementedError('Implement smallest_good_base')

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
