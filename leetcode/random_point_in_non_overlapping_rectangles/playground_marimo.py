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
    # 497. Random Point in Non-overlapping Rectangles

    **Medium** · Array, Math, Binary Search, Reservoir Sampling, Prefix Sum, Randomized

    You are given an array of non-overlapping axis-aligned rectangles `rects` where `rects[i] = [ai, bi, xi, yi]` indicates that `(ai, bi)` is the bottom-left corner point of the `ith` rectangle and `(xi, yi)` is the top-right corner point of the `ith` rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.

    Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.

    Note that an integer point is a point that has integer coordinates.

    Implement the `Solution` class:

    - `Solution(int[][] rects)` Initializes the object with the given rectangles `rects`.
    - `int[] pick()` Returns a random integer point `[u, v]` inside the space covered by one of the given rectangles.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/07/24/lc-pickrandomrec.jpg)

    ```
    Input
    ["Solution", "pick", "pick", "pick", "pick", "pick"]
    [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
    Output
    [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]

    Explanation
    Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
    solution.pick(); // return [1, -2]
    solution.pick(); // return [1, -1]
    solution.pick(); // return [-1, -2]
    solution.pick(); // return [-2, -2]
    solution.pick(); // return [0, 0]
    ```

    ## Constraints

    - `1 <= rects.length <= 100`
    - `rects[i].length == 4`
    - `-10^9 <= ai < xi <= 10^9`
    - `-10^9 <= bi < yi <= 10^9`
    - `xi - ai <= 2000`
    - `yi - bi <= 2000`
    - All the rectangles do not overlap.
    - At most `10^4` calls will be made to `pick`.

    **Follow up:** What is the time and space complexity of your solution? Could you do it with `O(log n)` pick time using binary search?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def __init__(self, rects: list[list[int]]) -> None:
            raise NotImplementedError('Implement __init__')

        def pick(self) -> list[int]:
            raise NotImplementedError('Implement pick')

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
