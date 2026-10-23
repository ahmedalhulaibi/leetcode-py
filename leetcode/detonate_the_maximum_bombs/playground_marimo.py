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
    # 2101. Detonate the Maximum Bombs

    **Medium** · Array, Math, Depth-First Search, Breadth-First Search, Graph Theory, Geometry

    You are given a list of bombs. The **range** of a bomb is defined as the area where its effect can be felt. This area is in the shape of a **circle** with the center as the location of the bomb.

    The bombs are represented by a **0-indexed** 2D integer array `bombs` where `bombs[i] = [x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub>]`. `x<sub>i</sub>` and `y<sub>i</sub>` denote the X-coordinate and Y-coordinate of the location of the `i<sup>th</sup>` bomb, whereas `r<sub>i</sub>` denotes the **radius** of its range.

    You may choose to detonate a **single** bomb. When a bomb is detonated, it will detonate **all bombs** that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

    Given the list of `bombs`, return *the **maximum** number of bombs that can be detonated if you are allowed to detonate **only one** bomb*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-3.png)

    ```
    Input: bombs = [[2,1,3],[6,1,4]]
    Output: 2
    Explanation:
    The above figure shows the positions and ranges of the 2 bombs.
    If we detonate the left bomb, the right bomb will not be affected.
    But if we detonate the right bomb, both bombs will be detonated.
    So the maximum bombs that can be detonated is max(1, 2) = 2.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-2.png)

    ```
    Input: bombs = [[1,1,5],[10,10,5]]
    Output: 1
    Explanation:
    Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/11/07/desmos-eg1.png)

    ```
    Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    Output: 5
    Explanation:
    The best bomb to detonate is bomb 0 because:
    - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
    - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
    - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
    Thus all 5 bombs are detonated.
    ```

    ## Constraints

    - 1 <= bombs.length <= 100
    - bombs[i].length == 3
    - 1 <= x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub> <= 10<sup>5</sup>

    **Follow up:** Can you solve it without building the graph explicitly?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_detonation(self, bombs: list[list[int]]) -> int:
            raise NotImplementedError('Implement maximum_detonation')

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
