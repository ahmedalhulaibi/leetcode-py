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
    # 935. Knight Dialer

    **Medium** · Dynamic Programming

    <p>The chess knight has a <strong>unique movement</strong>&nbsp;,it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an <strong>L</strong>). The possible movements of chess knight are shown in this diagram:</p>

    <p>A chess knight can move as indicated in the chess diagram below:</p>

    <p>We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell&nbsp;(i.e. blue cell).</p>

    <p><img alt="\" src="https://assets.leetcode.com/uploads/2020/08/18/chess.jpg" style="width: 402px; height: 402px;" /></p>

    <p><img alt="\" src="https://assets.leetcode.com/uploads/2020/08/18/phone.jpg" style="width: 282px; height: 302px;" /></p>

    <p>Given an integer <code>n</code>, return how many distinct phone numbers of length <code>n</code> we can dial.</p>

    <p>You are allowed to place the knight on any numeric cell initially and then you should perform <code>n - 1</code> jumps to dial a number of length <code>n</code>. All jumps should be valid knight jumps.</p>

    <p>As the answer may be very large, return the answer modulo <code>10<sup>9</sup> + 7</code>.</p>

    ## Examples

    ```
    Input: n = 1
    Output: 10
    Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
    ```

    ```
    Input: n = 2
    Output: 20
    Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
    ```

    ```
    Input: n = 3131
    Output: 136006598
    Explanation: Please take care of the mod.
    ```

    ## Constraints

    - 1 &lt;= n &lt;= 5000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def knight_dialer(self, n: int) -> int:
            raise NotImplementedError('Implement knight_dialer')

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
