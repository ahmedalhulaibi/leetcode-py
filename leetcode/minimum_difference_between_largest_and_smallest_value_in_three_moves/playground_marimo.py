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
    # 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

    **Medium** · Array, Greedy, Sorting

    <p>You are given an integer array <code>nums</code>.</p>

    <p>In one move, you can choose one element of <code>nums</code> and change it to <strong>any value</strong>.</p>

    <p>Return <em>the minimum difference between the largest and smallest value of </em><code>nums</code><em> <strong>after performing at most three moves</strong></em>.</p>

    ## Examples

    ```
    Input: nums = [5,3,2,4]
    Output: 0
    Explanation: We can make at most 3 moves.
    In the first move, change 2 to 3. nums becomes [5,3,3,4].
    In the second move, change 4 to 3. nums becomes [5,3,3,3].
    In the third move, change 5 to 3. nums becomes [3,3,3,3].
    After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
    ```

    ```
    Input: nums = [1,5,0,10,14]
    Output: 1
    Explanation: We can make at most 3 moves.
    In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
    In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
    In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
    After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
    It can be shown that there is no way to make the difference 0 in 3 moves.
    ```

    ```
    Input: nums = [3,100,20]
    Output: 0
    Explanation: We can make at most 3 moves.
    In the first move, change 100 to 7. nums becomes [3,7,20].
    In the second move, change 20 to 7. nums becomes [3,7,7].
    In the third move, change 3 to 7. nums becomes [7,7,7].
    After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.
    ```

    ## Constraints

    - 1 &lt;= nums.length &lt;= 10^5
    - -10^9 &lt;= nums[i] &lt;= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_difference(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement min_difference')

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
