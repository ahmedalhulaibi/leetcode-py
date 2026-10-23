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
    # 489. Robot Room Cleaner

    **Hard** · Backtracking, Interactive

    You are controlling a robot that is located somewhere in a room. The room is modeled as an `m x n` binary grid where `0` represents a wall and `1` represents an empty slot.

    The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API `Robot`.

    You are tasked to use the robot to clean the entire room (i.e. clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is `90` degrees.

    When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

    Design an algorithm to clean the entire room using the following APIs:

    ```
    interface Robot {
      // returns true if next cell is open and robot moves into the cell.
      // returns false if next cell is obstacle and robot stays on the current cell.
      boolean move();

      // Robot will stay on the same cell after calling turnLeft/turnRight.
      // Each turn will be 90 degrees.
      void turnLeft();
      void turn_right();

      // Clean the current cell.
      void clean();
    }
    ```

    **Note** that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0489.Robot%20Room%20Cleaner/images/lc-grid.jpg)

    ```
    Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
    Output: Robot cleaned all rooms.
    Explanation: All grids in the room are marked by either 0 or 1. 0 means the cell is blocked, while 1 means the cell is accessible. The robot initially starts at the position of row=1, col=3.
    ```

    ```
    Input: room = [[1]], row = 0, col = 0
    Output: Robot cleaned all rooms.
    ```

    ## Constraints

    - `m == room.length`
    - `n == room[i].length`
    - `1 <= m <= 100`
    - `1 <= n <= 200`
    - `room[i][j]` is either `0` or `1`.
    - `0 <= row < m`
    - `0 <= col < n`
    - `room[row][col] == 1`
    - All the empty cells can be visited from the starting position.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Robot:

        def __init__(self, room: list[list[int]], row: int, col: int) -> None:
            self.room = room
            self.row = row
            self.col = col
            self.direction = 0
            self.cleaned: set[tuple[int, int]] = set()

        def move(self) -> bool:
            dr = (-1, 0, 1, 0)[self.direction]
            dc = (0, 1, 0, -1)[self.direction]
            nr, nc = (self.row + dr, self.col + dc)
            if nr < 0 or nr >= len(self.room) or nc < 0 or (nc >= len(self.room[0])) or (self.room[nr][nc] == 0):
                return False
            self.row, self.col = (nr, nc)
            return True

        def turn_left(self) -> None:
            self.direction = (self.direction + 3) % 4

        def turn_right(self) -> None:
            self.direction = (self.direction + 1) % 4

        def clean(self) -> None:
            self.cleaned.add((self.row, self.col))

    class Solution:

        def clean_room(self, robot: Robot) -> None:
            raise NotImplementedError('Implement clean_room')

    practice_exports = {'Robot': Robot, 'Solution': Solution}
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
