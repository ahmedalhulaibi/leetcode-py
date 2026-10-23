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
    # 1462. Course Schedule IV

    **Medium** · Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort

    There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `ai` first if you want to take course `bi`.

    - For example, the pair `[0, 1]` indicates that you have to take course `0` before you can take course `1`.

    Prerequisites can also be **indirect**. If course `a` is a prerequisite of course `b`, and course `b` is a prerequisite of course `c`, then course `a` is a prerequisite of course `c`.

    You are also given an array `queries` where `queries[j] = [uj, vj]`. For the `jth` query, you should answer whether course `uj` is a prerequisite of course `vj` or not.

    Return *a boolean array* `answer`, *where* `answer[j]` *is the answer to the* `jth` *query*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg)

    ```
    Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
    Output: [false,true]
    Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
    Course 0 is not a prerequisite of course 1, but the opposite is true.
    ```

    ```
    Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
    Output: [false,false]
    Explanation: There are no prerequisites, and each course is independent.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/05/01/courses4-3-graph.jpg)

    ```
    Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
    Output: [true,true]
    ```

    ## Constraints

    - `2 <= numCourses <= 100`
    - `0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)`
    - `prerequisites[i].length == 2`
    - `0 <= ai, bi <= numCourses - 1`
    - `ai != bi`
    - All the pairs `[ai, bi]` are **unique**.
    - The prerequisites graph has no cycles.
    - `1 <= queries.length <= 10^4`
    - `0 <= ui, vi <= numCourses - 1`
    - `ui != vi`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def check_if_prerequisite(self, num_courses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
            raise NotImplementedError('Implement check_if_prerequisite')

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
