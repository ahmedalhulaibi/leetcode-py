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
    # 1359. Count All Valid Pickup and Delivery Options

    **Hard** · Math, Dynamic Programming, Combinatorics

    Given <code>n</code> orders, each order consists of a pickup and a delivery service.

    Count all valid pickup/delivery possible sequences such that delivery(i) is always after of&nbsp;pickup(i).&nbsp;

    Since the answer&nbsp;may be too large,&nbsp;return it modulo<code> 10<sup>9</sup> + 7</code>.

    ## Examples

    ```
    Input: n = 1
    Output: 1
    Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
    ```

    ```
    Input: n = 2
    Output: 6
    Explanation: All possible orders:
    (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
    This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
    ```

    ```
    Input: n = 3
    Output: 90
    ```

    ## Constraints

    - 1 <= n <= 500



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_orders(self, n: int) -> int:
            raise NotImplementedError('Implement count_orders')

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
