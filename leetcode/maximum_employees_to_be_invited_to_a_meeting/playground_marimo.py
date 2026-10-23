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
    # 2127. Maximum Employees to Be Invited to a Meeting

    **Hard** · Array, Dynamic Programming, Depth-First Search, Graph, Topological Sort

    A company is organizing a meeting and has a list of <code>n</code> employees, waiting to be invited. They have arranged for a large <strong>circular</strong> table, capable of seating <strong>any number</strong> of employees.</p>

    <p>The employees are numbered from <code>0</code> to <code>n - 1</code>. Each employee has a <strong>favorite</strong> person and they will attend the meeting <strong>only if</strong> they can sit next to their favorite person at the table. The favorite person of an employee is <strong>not</strong> themself.</p>

    <p>Given a <strong>0-indexed</strong> integer array <code>favorite</code>, where <code>favorite[i]</code> denotes the favorite person of the <code>i<sup>th</sup></code> employee, return <em>the <strong>maximum number of employees</strong> that can be invited to the meeting</em>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/12/14/ex1.png)

    ```
    Input: favorite = [2,2,1,2]
    Output: 3
    Explanation:
    The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
    All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
    Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
    The maximum number of employees that can be invited to the meeting is 3.
    ```

    ```
    Input: favorite = [1,2,0]
    Output: 3
    Explanation:
    Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
    The seating arrangement will be the same as that in the figure given in example 1:
    - Employee 0 will sit between employees 2 and 1.
    - Employee 1 will sit between employees 0 and 2.
    - Employee 2 will sit between employees 1 and 0.
    The maximum number of employees that can be invited to the meeting is 3.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/12/14/ex2.png)

    ```
    Input: favorite = [3,0,1,4,1]
    Output: 4
    Explanation:
    The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
    Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
    So the company leaves them out of the meeting.
    The maximum number of employees that can be invited to the meeting is 4.
    ```

    ## Constraints

    - n == favorite.length
    - 2 <= n <= 10^5
    - 0 <= favorite[i] <= n - 1
    - favorite[i] != i



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_invitations(self, favorite: list[int]) -> int:
            raise NotImplementedError('Implement maximum_invitations')

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
