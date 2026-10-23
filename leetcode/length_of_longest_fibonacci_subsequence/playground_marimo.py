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
    # 873. Length of Longest Fibonacci Subsequence

    **Medium** · Array, Hash Table, Dynamic Programming

    A sequence <code>x1, x2, ..., xn</code> is <em>Fibonacci-like</em> if:</p>

    <ul>
        <li><code>n &gt;= 3</code></li>
        <li><code>xi + xi+1 == xi+2</code> for all <code>i + 2 &lt;= n</code></li>
    </ul>

    <p>Given a <strong>strictly increasing</strong> array <code>arr</code> of positive integers forming a sequence, return <em>the length of the longest Fibonacci-like subsequence of</em> <code>arr</code>. If one does not exist, return <code>0</code>.</p>

    <p>A <em>subsequence</em> is derived from another sequence <code>arr</code> by deleting any number of elements (including none) from <code>arr</code>, without changing the order of the remaining elements. For example, <code>[3, 5, 8]</code> is a subsequence of <code>[3, 4, 5, 6, 7, 8]</code>.

    ## Examples

    ```
    Input: arr = [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation: The longest subsequence that is Fibonacci-like: [1,2,3,5,8].
    ```

    ```
    Input: arr = [1,3,7,11,12,14,18]
    Output: 3
    Explanation: The longest subsequence that is Fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
    ```

    ## Constraints

    - 3 <= arr.length <= 1000
    - 1 <= arr[i] < arr[i + 1] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def len_longest_fib_subsequence(self, arr: list[int]) -> int:
            raise NotImplementedError('Implement len_longest_fib_subsequence')

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
