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
    # 945. Minimum Increment to Make Array Unique

    **Medium** · Array, Greedy, Sorting, Counting

    <p>You are given an integer array <code>nums</code>. In one move, you can pick an index <code>i</code> where <code>0 &lt;= i &lt; nums.length</code> and increment <code>nums[i]</code> by <code>1</code>.</p>

    <p>Return <em>the minimum number of moves to make every value in </em><code>nums</code><em> <strong>unique</strong></em>.</p>

    <p>The test cases are generated so that the answer fits in a 32-bit integer.</p>

    ## Examples

    ```
    Input: nums = [1,2,2]
    Output: 1
    Explanation: After 1 move, the array could be [1, 2, 3].
    ```

    ```
    Input: nums = [3,2,1,2,1,7]
    Output: 6
    Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
    It can be shown that it is impossible for the array to have all unique values with 5 or less moves.
    ```

    ## Constraints

    - 1 &lt;= nums.length &lt;= 10^5
    - 0 &lt;= nums[i] &lt;= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_increment_for_unique(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement min_increment_for_unique')

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
