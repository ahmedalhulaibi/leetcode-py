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
    # 259. 3Sum Smaller

    **Medium** · Array, Two Pointers, Binary Search, Sorting

    Given an array of `n` integers `nums` and an integer `target`, find the number of index triplets `i`, `j`, `k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

    ## Examples

    ```
    Input: nums = [-2,0,1,3], target = 2
    Output: 2
    Explanation: Because there are two triplets which sums are less than 2:
    [-2,0,1]
    [-2,0,3]
    ```

    ```
    Input: nums = [], target = 0
    Output: 0
    ```

    ```
    Input: nums = [0], target = 0
    Output: 0
    ```

    ## Constraints

    - `n == nums.length`
    - `0 <= n <= 3500`
    - `-100 <= nums[i] <= 100`
    - `-100 <= target <= 100`
    - The input is generated such that the answer is less than or equal to `10^9`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def three_sum_smaller(self, nums: list[int], target: int) -> int:
            raise NotImplementedError('Implement three_sum_smaller')

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
