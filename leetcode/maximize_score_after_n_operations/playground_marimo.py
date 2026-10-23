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
    # 1799. Maximize Score After N Operations

    **Hard** · Array, Math, Dynamic Programming, Backtracking, Bit Manipulation, Number Theory, Bitmask

    <p>You are given <code>nums</code>, an array of positive integers of size <code>2 * n</code>. You must perform <code>n</code> operations on this array.</p>

    <p>In the <code>i<sup>th</sup></code> operation <strong>(1-indexed)</strong>, you will:</p>

    <ul>
        <li>Choose two elements, <code>x</code> and <code>y</code>.</li>
        <li>Receive a score of <code>i * gcd(x, y)</code>.</li>
        <li>Remove <code>x</code> and <code>y</code> from <code>nums</code>.</li>
    </ul>

    <p>Return <em>the maximum score you can receive after performing </em><code>n</code><em> operations.</em></p>

    <p>The function <code>gcd(x, y)</code> is the greatest common divisor of <code>x</code> and <code>y</code>.</p>

    ## Examples

    ```
    Input: nums = [1,2]
    Output: 1
    Explanation: The optimal choice of operations is:
    (1 * gcd(1, 2)) = 1
    ```

    ```
    Input: nums = [3,4,6,8]
    Output: 11
    Explanation: The optimal choice of operations is:
    (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
    ```

    ```
    Input: nums = [1,2,3,4,5,6]
    Output: 14
    Explanation: The optimal choice of operations is:
    (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
    ```

    ## Constraints

    - 1 &lt;= n &lt;= 7
    - nums.length == 2 * n
    - 1 &lt;= nums[i] &lt;= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_score(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement max_score')

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
