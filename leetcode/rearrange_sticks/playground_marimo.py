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
    # 1866. Number of Ways to Rearrange Sticks With K Sticks Visible

    **Hard** · Math, Dynamic Programming, Combinatorics

    There are `n` uniquely-sized sticks whose lengths are integers from `1` to `n`. You want to arrange the sticks such that **exactly** `k` sticks are **visible** from the left. A stick is **visible** from the left if there are no **longer** sticks to the **left** of it.

    For example, if the sticks are arranged `[1,3,2,5,4]`, then the sticks with lengths `1`, `3`, and `5` are visible from the left.

    Given `n` and `k`, return the **number** of such arrangements. Since the answer may be large, return it **modulo** `10^9 + 7`.

    ## Examples

    ```
    Input: n = 3, k = 2
    Output: 3
    Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that exactly 2 sticks are visible.
    The visible sticks are underlined.
    ```

    ```
    Input: n = 5, k = 5
    Output: 1
    Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are visible.
    The visible sticks are underlined.
    ```

    ```
    Input: n = 20, k = 11
    Output: 647427950
    Explanation: There are 647427950 (mod 10^9 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.
    ```

    ## Constraints

    - 1 <= n <= 1000
    - 1 <= k <= n



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def rearrange_sticks(self, n: int, k: int) -> int:
            raise NotImplementedError('Implement rearrange_sticks')

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
