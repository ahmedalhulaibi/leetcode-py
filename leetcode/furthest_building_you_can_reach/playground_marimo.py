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
    # 1642. Furthest Building You Can Reach

    **Medium** · Array, Greedy, Heap (Priority Queue)

    You are given an integer array `heights` representing the heights of buildings, some bricks, and some ladders.

    You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

    While moving from building `i` to building `i+1` (0-indexed),

    - If the current building's height is **greater than or equal** to the next building's height, you do **not** need a ladder or bricks.
    - If the current building's height is **less than** the next building's height, you can either use **one ladder** or `(h[i+1] - h[i])` **bricks**.

    Return *the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.*

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/27/q4.gif)

    ```
    Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    Output: 4
    Explanation: Starting at building 0, you can follow these steps:
    - Go to building 1 without using ladders nor bricks since 4 >= 2.
    - Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
    - Go to building 3 without using ladders nor bricks since 7 >= 6.
    - Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
    It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
    ```

    ```
    Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
    Output: 7
    ```

    ```
    Input: heights = [14,3,19,3], bricks = 17, ladders = 0
    Output: 3
    ```

    ## Constraints

    - 1 <= heights.length <= 10^5
    - 1 <= heights[i] <= 10^6
    - 0 <= bricks <= 10^9
    - 0 <= ladders <= heights.length



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def furthest_building(self, heights: list[int], bricks: int, ladders: int) -> int:
            raise NotImplementedError('Implement furthest_building')

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
