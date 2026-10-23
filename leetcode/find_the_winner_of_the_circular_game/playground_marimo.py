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
    mo.md(r"""
    # 1823. Find the Winner of the Circular Game

    **Medium** · Array, Math, Recursion, Queue, Simulation

    <p>There are <code>n</code> friends that are playing a game. The friends are sitting in a circle and are numbered from <code>1</code> to <code>n</code> in <strong>clockwise order</strong>. More formally, moving clockwise from the <code>i<sup>th</sup></code> friend brings you to the <code>(i+1)<sup>th</sup></code> friend for <code>1 &lt;= i &lt; n</code>, and moving clockwise from the <code>n<sup>th</sup></code> friend brings you to the <code>1<sup>st</sup></code> friend.</p>

    <p>The rules of the game are as follows:</p>

    <ol>
        <li><strong>Start</strong> at the <code>1<sup>st</sup></code> friend.</li>
        <li>Count the next <code>k</code> friends in the clockwise direction <strong>including</strong> the friend you started at. The counting wraps around the circle and may count some friends more than once.</li>
        <li>The last friend you counted leaves the circle and loses the game.</li>
        <li>If there is still more than one friend in the circle, go back to step <code>2</code> <strong>starting</strong> from the friend <strong>immediately clockwise</strong> of the friend who just lost and repeat.</li>
        <li>Else, the last friend in the circle wins the game.</li>
    </ol>

    <p>Given the number of friends, <code>n</code>, and an integer <code>k</code>, return <em>the winner of the game</em>.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/25/ic234-q2-ex11.png)

    ```
    Input: n = 5, k = 2
    Output: 3
    Explanation: Here are the steps of the game:
    1) Start at friend 1.
    2) Count 2 friends clockwise, which are friends 1 and 2.
    3) Friend 2 leaves the circle. Next start is friend 3.
    4) Count 2 friends clockwise, which are friends 3 and 4.
    5) Friend 4 leaves the circle. Next start is friend 5.
    6) Count 2 friends clockwise, which are friends 5 and 1.
    7) Friend 1 leaves the circle. Next start is friend 3.
    8) Count 2 friends clockwise, which are friends 3 and 5.
    9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
    ```

    ```
    Input: n = 6, k = 5
    Output: 1
    Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.
    ```

    ## Constraints

    - 1 &lt;= k &lt;= n &lt;= 500

    **Follow up:** Could you solve this problem in linear time with constant space?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_the_winner(self, n: int, k: int) -> int:
            raise NotImplementedError('Implement find_the_winner')

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
