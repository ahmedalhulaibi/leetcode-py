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
    # 286. Walls And Gates

    **Medium** · Array, Breadth-First Search, Matrix

    You are given a `m × n` 2D grid initialized with these three possible values:

    - `-1` - A wall or obstacle that can not be traversed.
    - `0` - A gate.
    - `INF` - Infinity an empty room. We use the value `2^31 - 1 = 2147483647` to represent `INF`.

    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with `INF`.

    **Follow up:** Can you solve it in-place and in O(m × n) time complexity?

    ## Examples

    ```
    Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    ```

    **Explanation:** the 2D grid is:

    ```
    INF  -1   0   INF
    INF  INF  INF  -1
    INF  -1   INF  -1
      0  -1   INF  INF
    ```
    the result is:
    ```
     3  -1   0   1
     2   2   1  -1
     1  -1   2  -1
     0  -1   3   4
    ```
    explanation: the gate is located at (0,2), (3,0), (3,3). the room at (0,0) is distance 3 from the nearest gate at (3,0).

    ```
    Input: rooms = [[0,-1],[2147483647,2147483647]]
    Output: [[0,-1],[1,2]]
    ```

    ## Constraints

    - `m == rooms.length`
    - `n == rooms[i].length`
    - `1 <= m, n <= 100`
    - `rooms[i][j]` is one of `-1`, `0`, or `2147483647`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def walls_and_gates(self, rooms: list[list[int]]) -> None:
            raise NotImplementedError('Implement walls_and_gates')

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
