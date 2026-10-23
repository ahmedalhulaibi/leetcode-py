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
    # 1057. Campus Bikes

    **Medium** · Array, Greedy, Sorting, Heap (Priority Queue)

    On a campus represented on the X-Y plane, there are `n` workers and `m` bikes, with `n <= m`.

    You are given an array `workers` of length `n` where `workers[i] = [xi, yi]` is the position of the `ith` worker. You are also given an array `bikes` of length `m` where `bikes[j] = [xj, yj]` is the position of the `jth` bike. All the given positions are **unique**.

    Assign a bike to each worker. Among the available bikes and workers, we choose the `(workeri, bikej)` pair with the shortest **Manhattan distance** between each other and assign the bike to that worker.

    If there are multiple `(workeri, bikej)` pairs with the same shortest **Manhattan distance**, we choose the pair with the **smallest worker index**. If there are multiple ways to do that, we choose the pair with the **smallest bike index**. Repeat this process until there are no available workers.

    Return an array `answer` of length `n`, where `answer[i]` is the index (**0-indexed**) of the bike that the `ith` worker is assigned to.

    The **Manhattan distance** between two points `p1` and `p2` is `Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|`.

    ## Examples

    ```
    Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
    Output: [1,0]
    Explanation: Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1.
    ```

    ```
    Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
    Output: [0,2,1]
    Explanation: Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1.
    ```

    ## Constraints

    - n == workers.length
    - m == bikes.length
    - 1 <= n <= m <= 1000
    - workers[i].length == bikes[j].length == 2
    - 0 <= xi, yi < 1000
    - 0 <= xj, yj < 1000
    - All worker and bike locations are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def assign_bikes(self, workers: list[list[int]], bikes: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement assign_bikes')

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
