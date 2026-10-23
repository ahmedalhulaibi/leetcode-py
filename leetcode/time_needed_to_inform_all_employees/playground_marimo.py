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
    # 1376. Time Needed to Inform All Employees

    **Medium** · Tree, Depth-First Search, Breadth-First Search

    A company has `n` employees with a unique ID for each employee from `0` to `n - 1`. The head of the company is the one with `headID`.

    Each employee has one direct manager given in the `manager` array where `manager[i]` is the direct manager of the `i-th` employee, `manager[headID] = -1`. Also, it is guaranteed that the subordination relationships have a tree structure.

    The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

    The `i-th` employee needs `informTime[i]` minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

    Return *the number of minutes* needed to inform all the employees about the urgent news.

    ## Examples

    ```
    Input: n = 1, headID = 0, manager = [-1], informTime = [0]
    Output: 0
    ```
    **Explanation:** The head of the company is the only employee in the company.

    ![Example 2](https://assets.leetcode.com/uploads/2020/02/27/graph.png)

    ```
    Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
    Output: 1
    ```
    **Explanation:** The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all. The tree structure of the employees in the company is shown.

    ## Constraints

    - `1 <= n <= 10^5`
    - `0 <= headID < n`
    - `manager.length == n`
    - `0 <= manager[i] < n`
    - `manager[headID] == -1`
    - `informTime.length == n`
    - `0 <= informTime[i] <= 1000`
    - `informTime[i] == 0` if employee `i` has no subordinates.
    - It is **guaranteed** that all the employees can be informed.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_of_minutes(self, n: int, head_id: int, manager: list[int], inform_time: list[int]) -> int:
            raise NotImplementedError('Implement num_of_minutes')

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
