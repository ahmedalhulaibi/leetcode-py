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
    # 587. Erect the Fence

    **Hard** · Array, Math, Geometry

    You are given an array `trees` where `trees[i] = [xi, yi]` represents the location of a tree in the garden.

    Fence the entire garden using the minimum length of rope, as it is expensive. The garden is well-fenced only if **all the trees are enclosed**.

    Return *the coordinates of trees that are exactly located on the fence perimeter*. You may return the answer in **any order**.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0587.Erect%20the%20Fence/images/erect2-plane.jpg)

    ```
    Input: trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
    Explanation: All the trees will be on the perimeter of the fence except the tree at [2, 2], which is inside the fence.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0587.Erect%20the%20Fence/images/erect1-plane.jpg)

    ```
    Input: trees = [[1,2],[2,2],[4,2]]
    Output: [[4,2],[2,2],[1,2]]
    Explanation: The fence forms a line that passes through all the trees.
    ```

    ## Constraints

    - `1 <= trees.length <= 3000`
    - `trees[i].length == 2`
    - `0 <= xi, yi <= 100`
    - All the given positions are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def outer_trees(self, trees: list[list[int]]) -> list[list[int]]:
            raise NotImplementedError('Implement outer_trees')

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
