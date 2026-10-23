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
    # 1964. Find the Longest Valid Obstacle Course at Each Position

    **Hard** · Array, Binary Search, Binary Indexed Tree, Longest Increasing Subsequence

    You want to build some obstacle courses. You are given a <strong>0-indexed</strong> integer array <code>obstacles</code> of length <code>n</code>, where <code>obstacles[i]</code> describes the height of the <code>i<sup>th</sup></code> obstacle.

    For every index <code>i</code> between <code>0</code> and <code>n - 1</code> (<strong>inclusive</strong>), find the length of the <strong>longest obstacle course</strong> in <code>obstacles</code> such that:

    <ul>
    <li>You choose any number of obstacles between <code>0</code> and <code>i</code> <strong>inclusive</strong>.</li>
    <li>You must include the <code>i<sup>th</sup></code> obstacle in the course.</li>
    <li>You must put the chosen obstacles in the <strong>same order</strong> as they appear in <code>obstacles</code>.</li>
    <li>Every obstacle (except the first) is <strong>taller</strong> than or the <strong>same height</strong> as the obstacle immediately before it.</li>
    </ul>

    Return <em>an array</em> <code>ans</code> <em>of length</em> <code>n</code>, <em>where</em> <code>ans[i]</code> <em>is the length of the <strong>longest obstacle course</strong> for index</em> <code>i</code><em> as described above</em>.

    ## Examples

    ```
    Input: obstacles = [1,2,3,2]
    Output: [1,2,3,3]
    Explanation: The longest valid obstacle course at each position is:
    - i = 0: [1], [1] has length 1.
    - i = 1: [1,2], [1,2] has length 2.
    - i = 2: [1,2,3], [1,2,3] has length 3.
    - i = 3: [1,2,3,2], [1,2,2] has length 3.
    ```

    ```
    Input: obstacles = [2,2,1]
    Output: [1,2,1]
    Explanation: The longest valid obstacle course at each position is:
    - i = 0: [2], [2] has length 1.
    - i = 1: [2,2], [2,2] has length 2.
    - i = 2: [2,2,1], [1] has length 1.
    ```

    ```
    Input: obstacles = [3,1,5,6,4,2]
    Output: [1,1,2,3,2,2]
    Explanation: The longest valid obstacle course at each position is:
    - i = 0: [3], [3] has length 1.
    - i = 1: [3,1], [1] has length 1.
    - i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
    - i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
    - i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
    - i = 5: [3,1,5,6,4,2], [1,2] has length 2.
    ```

    ## Constraints

    - n == obstacles.length
    - 1 <= n <= 10^5
    - 1 <= obstacles[i] <= 10^7



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def longest_obstacle_course(self, obstacles: list[int]) -> list[int]:
            raise NotImplementedError('Implement longest_obstacle_course')

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
