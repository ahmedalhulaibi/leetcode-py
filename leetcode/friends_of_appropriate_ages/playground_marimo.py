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
    # 825. Friends Of Appropriate Ages

    **Medium** · Array, Two Pointers, Binary Search, Sorting

    <p>There are <code>n</code> persons on a social media website. You are given an integer array <code>ages</code> where <code>ages[i]</code> is the age of the <code>i<sup>th</sup></code> person.</p>

    <p>A Person <code>x</code> will not send a friend request to a person <code>y</code> (<code>x != y</code>) if any of the following conditions is true:</p>

    <ul>
        <li><code>age[y] &lt;= 0.5 * age[x] + 7</code></li>
        <li><code>age[y] &gt; age[x]</code></li>
        <li><code>age[y] &gt; 100 &amp;&amp; age[x] &lt; 100</code></li>
    </ul>

    <p>Otherwise, <code>x</code> will send a friend request to <code>y</code>.</p>

    <p>Note that if <code>x</code> sends a request to <code>y</code>, <code>y</code> will not necessarily send a request to <code>x</code>. Also, a person will not send a friend request to themself.</p>

    <p>Return <em>the total number of friend requests made</em>.</p>

    <p>&nbsp;</p>

    ## Examples

    ```
    Input: ages = [16,16]
    Output: 2
    Explanation: 2 people friend request each other.
    ```

    ```
    Input: ages = [16,17,18]
    Output: 2
    Explanation: Friend requests are made 17 -> 16, 18 -> 17.
    ```

    ```
    Input: ages = [20,30,100,110,120]
    Output: 3
    Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
    ```

    ## Constraints

    - n == ages.length
    - 1 <= n <= 2 * 10^4
    - 1 <= ages[i] <= 120



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_friend_requests(self, ages: list[int]) -> int:
            raise NotImplementedError('Implement num_friend_requests')

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
