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
    # 2563. Count the Number of Fair Pairs

    **Medium** · Array, Two Pointers, Binary Search, Sorting

    Given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>n</code> and two integers <code>lower</code> and <code>upper</code>, return <em>the number of <strong>fair pairs</strong></em>.

    A pair <code>(i, j)</code> is <strong>fair</strong> if:

    <ul>
    <li><code>0 &lt;= i &lt; j &lt; n</code>, and</li>
    <li><code>lower &lt;= nums[i] + nums[j] &lt;= upper</code></li>
    </ul>

    ## Examples

    ```
    Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
    Output: 6
    ```
    **Explanation:** There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

    ```
    Input: nums = [1,7,9,2,5], lower = 11, upper = 11
    Output: 1
    ```
    **Explanation:** There is a single fair pair: (2,3).

    ## Constraints

    - 1 <= nums.length <= 10^5
    - nums.length == n
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= lower <= upper <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_fair_pairs(self, nums: list[int], lower: int, upper: int) -> int:
            raise NotImplementedError('Implement count_fair_pairs')

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
