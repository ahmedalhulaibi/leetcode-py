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
    # 207. Course Schedule

    **Medium** · Depth-First Search, Breadth-First Search, Graph, Topological Sort

    There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

    - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

    Return `true` if you can finish all courses. Otherwise, return `false`.

    ## Examples

    ```
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    ```
    **Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

    ```
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    ```
    **Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

    ## Constraints

    - `1 <= numCourses <= 2000`
    - `0 <= prerequisites.length <= 5000`
    - `prerequisites[i].length == 2`
    - `0 <= ai, bi < numCourses`
    - All the pairs prerequisites[i] are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
            raise NotImplementedError('Implement can_finish')

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
