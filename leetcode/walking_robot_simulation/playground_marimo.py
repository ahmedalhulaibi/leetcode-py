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
    mo.md(r"""
    # 874. Walking Robot Simulation

    **Medium** · Array, Hash Table, Simulation

    A robot on an infinite XY-plane starts at point <code>(0, 0)</code> facing north. The robot receives an array of integers <code>commands</code>, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:</p>

    <ul>
        <li><code>-2</code>: Turn left 90 degrees.</li>
        <li><code>-1</code>: Turn right 90 degrees.</li>
        <li><code>1 &lt;= k &lt;= 9</code>: Move forward <code>k</code> units, one unit at a time.</li>
    </ul>

    <p>Some of the grid squares are obstacles. The <code>ith</code> obstacle is at grid point <code>obstacles[i] = (xi, yi)</code>. If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.</p>

    <p>Return <em>the maximum squared Euclidean distance that the robot reaches at any point in its path</em>.</p>

    ## Examples

    ```
    Input: commands = [4,-1,3], obstacles = []
    Output: 25
    Explanation: The robot starts at (0, 0):
    1. Move north 4 units to (0, 4).
    2. Turn right to face east.
    3. Move east 3 units to (3, 4).
    The furthest point the robot ever gets from the origin is (3, 4), which squared is 3^2 + 4^2 = 25 units away.
    ```

    ```
    Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
    Output: 65
    Explanation: The robot is being tracked:
    1. Move north 4 units to (0, 4).
    2. Turn right to face east.
    3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
    4. Turn left to face north.
    5. Move north 4 units to (1, 8).
    The furthest point the robot ever gets from the origin is (1, 8), which squared is 1^2 + 8^2 = 65 units away.
    ```

    ```
    Input: commands = [6,-1,-1,6], obstacles = []
    Output: 36
    Explanation: The robot starts at (0, 0):
    1. Move north 6 units to (0, 6).
    2. Turn right to face east.
    3. Turn right to face south.
    4. Move south 6 units to (0, 0).
    The furthest point the robot ever gets from the origin is (0, 6), which squared is 6^2 = 36 units away.
    ```

    ## Constraints

    - 1 <= commands.length <= 10^4
    - commands[i] is either -2, -1, or an integer in the range [1, 9].
    - 0 <= obstacles.length <= 10^4
    - -3 * 10^4 <= xi, yi <= 3 * 10^4
    - The answer is guaranteed to be less than 2^31.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def robot_sim(self, commands: list[int], obstacles: list[list[int]]) -> int:
            raise NotImplementedError('Implement robot_sim')

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
