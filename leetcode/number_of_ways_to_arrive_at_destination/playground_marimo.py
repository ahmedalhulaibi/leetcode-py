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
    # 1976. Number of Ways to Arrive at Destination

    **Medium** · Dynamic Programming, Graph Theory, Topological Sort, Shortest Path, Dijkstra's Algorithm

    You are in a city that consists of `n` intersections numbered from `0` to `n - 1` with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

    You are given an integer `n` and a 2D integer array `roads` where `roads[i] = [u<sub>i</sub>, v<sub>i</sub>, time<sub>i</sub>]` means that there is a road between intersections `u<sub>i</sub>` and `v<sub>i</sub>` that takes `time<sub>i</sub>` minutes to travel. You want to know in how many ways you can travel from intersection `0` to intersection `n - 1` in the **shortest amount of time**.

    Return _the **number of ways** you can arrive at your destination in the **shortest amount of time**_. Since the answer may be large, return it **modulo** `10<sup>9</sup> + 7`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2025/02/14/1976_corrected.png)

    ```
    Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    Output: 4
    Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
    The four ways to get there in 7 minutes are:
    - 0 ➝ 6
    - 0 ➝ 4 ➝ 6
    - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
    - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
    ```

    ```
    Input: n = 2, roads = [[1,0,10]]
    Output: 1
    Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
    ```

    ## Constraints

    - 1 <= n <= 200
    - n - 1 <= roads.length <= n * (n - 1) / 2
    - roads[i].length == 3
    - 0 <= u<sub>i</sub>, v<sub>i</sub> <= n - 1
    - 1 <= time<sub>i</sub> <= 10<sup>9</sup>
    - u<sub>i</sub> != v<sub>i</sub>
    - There is at most one road connecting any two intersections.
    - You can reach any intersection from any other intersection.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import heapq

    class Solution:

        def count_paths(self, n: int, roads: list[list[int]]) -> int:
            raise NotImplementedError('Implement count_paths')

    practice_exports = {'heapq': heapq, 'Solution': Solution}
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
