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
    # 2050. Parallel Courses III

    **Hard** · Array, Dynamic Programming, Graph Theory, Topological Sort, Directed Acyclic Graph

    You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given a 2D integer array `relations` where `relations[j] = [prevCourse_j, nextCourse_j]` denotes that course `prevCourse_j` has to be completed **before** course `nextCourse_j` (prerequisite relationship). Furthermore, you are given a **0-indexed** integer array `time` where `time[i]` denotes how many **months** it takes to complete the `(i+1)th` course.

    You must find the **minimum** number of months needed to complete all the courses following these rules:

    - You may start taking a course at **any time** if the prerequisites are met.
    - **Any number of courses** can be taken at the **same time**.

    Return *the **minimum** number of months needed to complete all the courses*.

    **Note:** The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/10/07/ex1.png)

    ```
    Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
    Output: 8
    ```
    **Explanation:** We start course 1 and course 2 simultaneously at month 0. Course 1 takes 3 months and course 2 takes 2 months to complete respectively. Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.

    ![Example 2](https://assets.leetcode.com/uploads/2021/10/07/ex2.png)

    ```
    Input: n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
    Output: 12
    ```
    **Explanation:** Courses 1, 2 and 3 run in parallel and finish after 1, 2 and 3 months. Course 4 starts after course 3 and finishes at month 7. Course 5 starts at month 7 and finishes at month 12.

    ## Constraints

    - `1 <= n <= 5 * 10^4`
    - `0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)`
    - `relations[j].length == 2`
    - `1 <= prevCourse_j, nextCourse_j <= n`
    - `prevCourse_j != nextCourse_j`
    - All the pairs `[prevCourse_j, nextCourse_j]` are **unique**.
    - `time.length == n`
    - `1 <= time[i] <= 10^4`
    - The given graph is a directed acyclic graph.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_time(self, n: int, relations: list[list[int]], time: list[int]) -> int:
            raise NotImplementedError('Implement minimum_time')

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
