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
    # 1498. Number of Subsequences That Satisfy the Given Sum Condition

    **Medium** · Array, Two Pointers, Binary Search, Sorting

    You are given an array of integers `nums` and an integer `target`.

    Return *the number of **non-empty** subsequences of* `nums` *such that the sum of the minimum and maximum element on it is less or equal to* `target`. Since the answer may be too large, return it **modulo** `10^9 + 7`.

    ## Examples

    ```
    Input: nums = [3,5,6,7], target = 9
    Output: 4
    Explanation: There are 4 subsequences that satisfy the condition.
    [3] -> Min value + max value <= target (3 + 3 <= 9)
    [3,5] -> (3 + 5 <= 9)
    [3,5,6] -> (3 + 6 <= 9)
    [3,6] -> (3 + 6 <= 9)
    ```

    ```
    Input: nums = [3,3,6,8], target = 10
    Output: 6
    Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
    [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
    ```

    ```
    Input: nums = [2,3,3,4,6,7], target = 12
    Output: 61
    Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
    Number of valid subsequences (63 - 2 = 61).
    ```

    ## Constraints

    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^6
    - 1 <= target <= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_subseq(self, nums: list[int], target: int) -> int:
            raise NotImplementedError('Implement num_subseq')

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
