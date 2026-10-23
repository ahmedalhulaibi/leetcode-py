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
    # 879. Profitable Schemes

    **Hard** · Array, Dynamic Programming, Knapsack Problem, 0-1 Knapsack

    There is a group of <code>n</code> members, and a list of various crimes they could commit. The <code>ith</code> crime generates a <code>profit[i]</code> and requires <code>group[i]</code> members to participate in it. If a member participates in one crime, that member can't participate in another crime.</p>

    <p>Let's call a <em>profitable scheme</em> any subset of these crimes that generates at least <code>minProfit</code> profit, and the total number of members participating in that subset of crimes is at most <code>n</code>.</p>

    <p>Return the number of schemes that can be chosen. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.

    ## Examples

    ```
    Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
    Output: 2
    Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
    In total, there are 2 schemes.
    ```

    ```
    Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
    Output: 7
    Explanation: Every subset of the crimes has total members at most 10 and profit at least 5,
    and 7 subsets exist, so all of them are profitable schemes.
    ```

    ## Constraints

    - 1 <= n <= 100
    - 0 <= minProfit <= 100
    - 1 <= group.length <= 100
    - 1 <= group[i] <= 100
    - profit.length == group.length
    - 0 <= profit[i] <= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def profitable_schemes(self, n: int, min_profit: int, group: list[int], profit: list[int]) -> int:
            raise NotImplementedError('Implement profitable_schemes')

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
