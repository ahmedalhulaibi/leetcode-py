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
    # 690. Employee Importance

    **Medium** · Array, Hash Table, Tree, Depth-First Search, Breadth-First Search

    You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

    You are given an array of employees `employees` where:

    - `employees[i].id` is the ID of the `i^th` employee.
    - `employees[i].importance` is the importance value of the `i^th` employee.
    - `employees[i].subordinates` is a list of the IDs of the direct subordinates of the `i^th` employee.

    Given an integer `id` that represents an employee's ID, return *the **total** importance value of this employee and all their direct and indirect subordinates*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/31/emp1-tree.jpg)

    ```
    Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
    Output: 11
    Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3. They both have an importance value of 3. Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/05/31/emp2-tree.jpg)

    ```
    Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
    Output: -3
    Explanation: Employee 5 has an importance value of -3 and has no direct subordinates. Thus, the total importance value of employee 5 is -3.
    ```

    ## Constraints

    - `1 <= employees.length <= 2000`
    - `1 <= employees[i].id <= 2000`
    - All `employees[i].id` are **unique**.
    - `-100 <= employees[i].importance <= 100`
    - One employee has at most one direct leader and may have several subordinates.
    - The IDs in `employees[i].subordinates` are **valid** IDs.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Employee:

        def __init__(self, id: int, importance: int, subordinates: list[int] | None=None) -> None:
            self.id = id
            self.importance = importance
            self.subordinates = subordinates if subordinates is not None else []

    class Solution:

        def get_importance(self, employees: list[Employee], id: int) -> int:
            raise NotImplementedError('Implement get_importance')

    practice_exports = {'Employee': Employee, 'Solution': Solution}
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
