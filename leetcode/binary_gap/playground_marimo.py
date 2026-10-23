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
    # 868. Binary Gap

    **Easy** · Bit Manipulation

    Given a positive integer `n`, find and return *the **longest distance** between any two **adjacent*** `1`*'s in the binary representation of* `n`. If there are no two adjacent `1`'s, return `0`.

    Two `1`'s are **adjacent** if there are only `0`'s separating them (possibly no `0`'s). The **distance** between two `1`'s is the absolute difference between their bit positions. For example, the two `1`'s in `"1001"` have a distance of 3.

    ## Examples

    ```
    Input: n = 22
    Output: 2
    ```
    **Explanation:** 22 in binary is `"10110"`.
    The first adjacent pair of 1's is `"10110"` with a distance of 2.
    The second adjacent pair of 1's is `"10110"` with a distance of 1.
    The answer is the largest of these two distances, which is 2.
    Note that `"10110"` is not a valid pair since there is a 1 separating the two 1's underlined.

    ```
    Input: n = 8
    Output: 0
    ```
    **Explanation:** 8 in binary is `"1000"`.
    There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

    ```
    Input: n = 5
    Output: 2
    ```
    **Explanation:** 5 in binary is `"101"`.

    ## Constraints

    - 1 <= n <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def binary_gap(self, n: int) -> int:
            raise NotImplementedError('Implement binary_gap')

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
