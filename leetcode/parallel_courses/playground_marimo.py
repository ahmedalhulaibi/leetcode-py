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
    # 1136. Parallel Courses

    **Medium** · Graph, Topological Sort

    You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where `relations[i] = [prevCourse_i, nextCourse_i]`, representing a prerequisite relationship between course `prevCourse_i` and course `nextCourse_i`: course `prevCourse_i` has to be taken before course `nextCourse_i`.

    In one semester, you can take **any number** of courses as long as you have taken all the prerequisites in the **previous** semester for the courses you are taking.

    Return *the **minimum** number of semesters needed to take all courses*. If there is no way to take all the courses, return `-1`.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1136.Parallel%20Courses/images/course1graph.jpg)

    ```
    Input: n = 3, relations = [[1,3],[2,3]]
    Output: 2
    ```
    **Explanation:** In the first semester, you can take courses 1 and 2. In the second semester, you can take course 3.

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1136.Parallel%20Courses/images/course2graph.jpg)

    ```
    Input: n = 3, relations = [[1,2],[2,3],[3,1]]
    Output: -1
    ```
    **Explanation:** No course can be studied because they are prerequisites of each other.

    ## Constraints

    - `1 <= n <= 5000`
    - `1 <= relations.length <= 5000`
    - `relations[i].length == 2`
    - `1 <= prevCourse_i, nextCourse_i <= n`
    - `prevCourse_i != nextCourse_i`
    - All the pairs `[prevCourse_i, nextCourse_i]` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_semesters(self, n: int, relations: list[list[int]]) -> int:
            raise NotImplementedError('Implement minimum_semesters')

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
