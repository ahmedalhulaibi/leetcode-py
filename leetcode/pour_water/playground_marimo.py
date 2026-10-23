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
    # 755. Pour Water

    **Medium** · Array, Simulation

    You are given an elevation map represented as an integer array `heights` where `heights[i]` representing the height of the terrain at index `i`. The width at each index is `1`. You are also given two integers `volume` and `k`. `volume` units of water will fall at index `k`.

    Water first drops at the index `k` and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

    - If the droplet would eventually fall by moving left, then move left.
    - Otherwise, if the droplet would eventually fall by moving right, then move right.
    - Otherwise, rise to its current position.

    Here, **"eventually fall"** means that the droplet will eventually be at a lower level if it moves in that direction. Also, level means the height of the terrain plus any water in that column.

    We can assume there is infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than one grid block, and each unit of water has to be in exactly one block.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0755.Pour%20Water/images/pour11-grid.jpg)

    ```
    Input: heights = [2,1,1,2,1,2,2], volume = 4, k = 3
    Output: [2,2,2,3,2,2,2]
    ```
    **Explanation:** The first drop of water lands at index k = 3. When moving left or right, the water can only move to the same level or a lower level. (By level, we mean the total height of the terrain plus any water in that column.) Since moving left will eventually make it fall, it moves left. Since moving left will not make it fall, it stays in place. The next droplet falls at index k = 3. Since the new droplet moving left will eventually make it fall, it moves left. Notice that the droplet still preferred to move left, even though it could move right (and moving right makes it fall quicker.) The third droplet falls at index k = 3. Since moving left would not eventually make it fall, it tries to move right. Since moving right would eventually make it fall, it moves right. Finally, the fourth droplet falls at index k = 3. Since moving left would not eventually make it fall, it tries to move right. Since moving right would not eventually make it fall, it stays in place.

    ```
    Input: heights = [1,2,3,4], volume = 2, k = 2
    Output: [2,3,3,4]
    ```
    **Explanation:** The last droplet settles at index 1, since moving further left would not cause it to eventually fall to a lower height.

    ```
    Input: heights = [3,1,3], volume = 5, k = 1
    Output: [4,4,4]
    ```

    ## Constraints

    - `1 <= heights.length <= 100`
    - `0 <= heights[i] <= 99`
    - `0 <= volume <= 2000`
    - `0 <= k < heights.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def pour_water(self, heights: list[int], volume: int, k: int) -> list[int]:
            raise NotImplementedError('Implement pour_water')

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
