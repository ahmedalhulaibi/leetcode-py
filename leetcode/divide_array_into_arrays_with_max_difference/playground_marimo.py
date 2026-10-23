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
    # 2966. Divide Array Into Arrays With Max Difference

    **Medium** · Array, Greedy, Sorting

    You are given an integer array `nums` of size `n` where `n` is a multiple of 3 and a positive integer `k`.

    Divide the array `nums` into `n / 3` arrays of size **3** satisfying the following condition:

    - The difference between **any** two elements in one array is **less than or equal** to `k`.

    Return a **2D** array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return **any** of them.

    ## Examples

    ```
    Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
    Output: [[1,1,3],[3,4,5],[7,8,9]]
    Explanation: The difference between any two elements in each array is less than or equal to 2.
    ```

    ```
    Input: nums = [2,4,2,2,5,2], k = 2
    Output: []
    Explanation: Because there are four 2s there will be an array with the elements 2 and 5 no matter how we divide it. Since 5 - 2 = 3 > k, the condition is not satisfied and so there is no valid division.
    ```

    ```
    Input: nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
    Output: [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]
    Explanation: The difference between any two elements in each array is less than or equal to 14.
    ```

    ## Constraints

    - `n == nums.length`
    - `1 <= n <= 10^5`
    - `n` is a multiple of 3
    - `1 <= nums[i] <= 10^5`
    - `1 <= k <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def divide_array(self, nums: list[int], k: int) -> list[list[int]]:
            raise NotImplementedError('Implement divide_array')

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
