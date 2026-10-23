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
    # 582. Kill Process

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Array, Hash Table

    You have `n` processes forming a rooted tree structure. You are given two integer arrays `pid` and `ppid`, where `pid[i]` is the ID of the `i^th` process and `ppid[i]` is the ID of the `i^th` process's parent process.

    Each process has only **one parent process** but may have multiple children processes. Only one process has `ppid[i] = 0`, which means this process has **no parent process** (the root of the tree).

    When a process is **killed**, all of its children processes will also be killed.

    Given an integer `kill` representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in **any order**.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0582.Kill%20Process/images/ptree.jpg)

    ```
    Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
    Output: [5,10]
    Explanation: The processes colored in red are the processes that should be killed.
    ```

    ```
    Input: pid = [1], ppid = [0], kill = 1
    Output: [1]
    ```

    ## Constraints

    - `n == pid.length`
    - `n == ppid.length`
    - `1 <= n <= 5 * 10^4`
    - `1 <= pid[i] <= 5 * 10^4`
    - `0 <= ppid[i] <= 5 * 10^4`
    - Only one process has no parent.
    - All the values of `pid` are **unique**.
    - `kill` is **guaranteed** to be in `pid`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def kill_process(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
            raise NotImplementedError('Implement kill_process')

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
