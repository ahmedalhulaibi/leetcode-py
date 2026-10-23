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
    # 789. Escape The Ghosts

    **Medium** · Array, Math

    You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point `[0, 0]`, and you are given a destination point `target = [xtarget, ytarget]` that you are trying to get to. There are several ghosts on the map with their starting positions given as a 2D array `ghosts`, where `ghosts[i] = [xi, yi]` represents the starting position of the ith ghost. All inputs are **integral coordinates**.

    Each turn, you and all the ghosts may independently choose to either **move 1 unit** in any of the four cardinal directions: north, east, south, or west, or **stay still**. All actions happen **simultaneously**.

    You escape if and only if you can reach the target **before** any ghost reaches you. If you reach any square (including the target) at the **same time** as a ghost, it **does not** count as an escape.

    Return `true` if it is possible to escape regardless of how the ghosts move, otherwise return `false`.

    ## Examples

    ```
    Input: ghosts = [[1,0],[0,3]], target = [0,1]
    Output: true
    ```
    **Explanation:** You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.

    ```
    Input: ghosts = [[1,0]], target = [2,0]
    Output: false
    ```
    **Explanation:** You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

    ```
    Input: ghosts = [[2,0]], target = [1,0]
    Output: false
    ```
    **Explanation:** The ghost can reach the target at the same time as you.

    ## Constraints

    - 1 <= ghosts.length <= 100
    - ghosts[i].length == 2
    - -10^4 <= xi, yi <= 10^4
    - There can be multiple ghosts in the same location.
    - target.length == 2
    - -10^4 <= xtarget, ytarget <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def escape_ghosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
            raise NotImplementedError('Implement escape_ghosts')

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
