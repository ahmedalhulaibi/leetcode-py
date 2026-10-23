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
    # 675. Cut Off Trees for Golf Event

    **Hard** · Array, Breadth-First Search, Heap (Priority Queue), Matrix

    You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an `m x n` matrix. In this matrix:

    - `0` means the cell cannot be walked through.
    - `1` represents an empty cell that can be walked through.
    - A number greater than `1` represents a tree in a cell that can be walked through, and this number is the tree's height.

    In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

    You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes `1` (an empty cell).

    Starting from the point `(0, 0)`, return *the minimum steps you need to walk to cut off all the trees*. If you cannot cut off all the trees, return `-1`.

    Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/11/26/trees1.jpg)

    ```
    Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
    Output: 6
    ```
    **Explanation:** Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.

    ![Example 2](https://assets.leetcode.com/uploads/2020/11/26/trees2.jpg)

    ```
    Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
    Output: -1
    ```
    **Explanation:** The trees in the bottom row cannot be accessed as the middle row is blocked.

    ```
    Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
    Output: 6
    ```
    **Explanation:** You can follow the same path as Example 1 to cut off all the trees. Note that you can cut off the first tree at (0, 0) before making any steps.

    ## Constraints

    - `m == forest.length`
    - `n == forest[i].length`
    - `1 <= m, n <= 50`
    - `0 <= forest[i][j] <= 10^9`
    - Heights of all trees are distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class Solution:

        def cut_off_tree(self, forest: list[list[int]]) -> int:
            raise NotImplementedError('Implement cut_off_tree')

    practice_exports = {'deque': deque, 'Solution': Solution}
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
