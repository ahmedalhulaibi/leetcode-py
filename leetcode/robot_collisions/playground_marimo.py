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
    # 2751. Robot Collisions

    **Hard** · Array, Stack, Sorting, Simulation

    There are n 1-indexed robots, each having a position on a line, health, and movement direction.

    You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

    All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

    If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

    Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

    Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

    Note: The positions may be unsorted.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/05/15/image-20230516011718-12.png)

    ```
    Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
    Output: [2,17,9,15,10]
    Explanation: No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2023/05/15/image-20230516004433-7.png)

    ```
    Input: positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
    Output: [14]
    Explanation: There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4's health is smaller, it gets removed, and robot 3's health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2023/05/15/image-20230516005114-9.png)

    ```
    Input: positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"
    Output: []
    Explanation: Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].
    ```

    ## Constraints

    - 1 <= positions.length == healths.length == directions.length == n <= 10^5
    - 1 <= positions[i], healths[i] <= 10^9
    - `directions[i]` is `'L'` or `'R'`
    - All values in `positions` are distinct



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def survived_robots_healths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
            raise NotImplementedError('Implement survived_robots_healths')

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
