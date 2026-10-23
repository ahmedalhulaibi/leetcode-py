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
    # 465. Optimal Account Balancing

    **Hard** · Bit Manipulation, Array, Dynamic Programming, Backtracking, Bitmask

    You are given an array of transactions `transactions` where `transactions[i] = [from_i, to_i, amount_i]` indicates that the person with `ID = from_i` gave `amount_i $` to the person with `ID = to_i`.

    Return the minimum number of transactions required to settle the debt.

    ## Examples

    ```
    Input: transactions = [[0,1,10],[2,0,5]]
    Output: 2
    Explanation:
    Person #0 gave person #1 $10.
    Person #2 gave person #0 $5.
    Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
    ```

    ```
    Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
    Output: 1
    Explanation:
    Person #0 gave person #1 $10.
    Person #1 gave person #0 $1.
    Person #1 gave person #2 $5.
    Person #2 gave person #0 $5.
    Therefore, person #1 only need to give person #0 $4, and all debt is settled.
    ```

    ## Constraints

    - `1 <= transactions.length <= 8`
    - `transactions[i].length == 3`
    - `0 <= from_i, to_i < 12`
    - `from_i != to_i`
    - `1 <= amount_i <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_transfers(self, transactions: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_transfers')

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
