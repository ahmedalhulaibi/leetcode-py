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
    # 1041. Robot Bounded In Circle

    **Medium** · Math, String, Simulation

    On an infinite plane, a robot initially stands at `(0, 0)` and faces north. Note that:

    - The north direction is the positive direction of the y-axis.
    - The south direction is the negative direction of the y-axis.
    - The east direction is the positive direction of the x-axis.
    - The west direction is the negative direction of the x-axis.

    The robot can receive one of three instructions:

    - `"G"`: go straight 1 unit.
    - `"L"`: turn 90 degrees to the left (i.e., anti-clockwise direction).
    - `"R"`: turn 90 degrees to the right (i.e., clockwise direction).

    The robot performs the `instructions` given in order, and repeats them forever.

    Return `true` if and only if there exists a circle in the plane such that the robot never leaves the circle.

    ## Examples

    ```
    Input: instructions = "GGLLGG"
    Output: true
    Explanation: The robot is initially at (0, 0) facing the north direction.
    "G": move one step. Position: (0, 1). Direction: North.
    "G": move one step. Position: (0, 2). Direction: North.
    "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
    "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
    "G": move one step. Position: (0, 1). Direction: South.
    "G": move one step. Position: (0, 0). Direction: South.
    Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
    Based on that, we return true.
    ```

    ```
    Input: instructions = "GG"
    Output: false
    Explanation: The robot is initially at (0, 0) facing the north direction.
    "G": move one step. Position: (0, 1). Direction: North.
    "G": move one step. Position: (0, 2). Direction: North.
    Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
    Based on that, we return false.
    ```

    ```
    Input: instructions = "GL"
    Output: true
    Explanation: The robot is initially at (0, 0) facing the north direction.
    "G": move one step. Position: (0, 1). Direction: North.
    "L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
    "G": move one step. Position: (-1, 1). Direction: West.
    "L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
    "G": move one step. Position: (-1, 0). Direction: South.
    "L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
    "G": move one step. Position: (0, 0). Direction: East.
    "L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
    Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
    Based on that, we return true.
    ```

    ## Constraints

    - `1 <= instructions.length <= 100`
    - `instructions[i]` is `'G'`, `'L'` or, `'R'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_robot_bounded(self, instructions: str) -> bool:
            raise NotImplementedError('Implement is_robot_bounded')

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
