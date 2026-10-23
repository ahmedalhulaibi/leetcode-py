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
    # 1235. Maximum Profit in Job Scheduling

    **Hard** · Array, Binary Search, Dynamic Programming, Sorting

    We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

    You're given the `startTime`, `endTime` and `profit` arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

    If you choose a job that ends at time `X` you will be able to start another job that starts at time `X`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png)

    ```
    Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
    Output: 120
    ```
    **Explanation:** The subset chosen is the first and fourth job. Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

    ![Example 2](https://assets.leetcode.com/uploads/2019/10/10/sample22_1584.png)

    ```
    Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
    Output: 150
    ```
    **Explanation:** The subset chosen is the first, fourth and fifth job. Profit obtained 150 = 20 + 70 + 60.

    ![Example 3](https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png)

    ```
    Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
    Output: 6
    ```

    ## Constraints

    - `1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4`
    - `1 <= startTime[i] < endTime[i] <= 10^9`
    - `1 <= profit[i] <= 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def job_scheduling(self, start_time: list[int], end_time: list[int], profit: list[int]) -> int:
            raise NotImplementedError('Implement job_scheduling')

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
