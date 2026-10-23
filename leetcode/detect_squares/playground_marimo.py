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
    # 2013. Detect Squares

    **Medium** · Array, Hash Table, Design, Counting, Data Stream

    You are given a stream of points on the X-Y plane. Design an algorithm that:

    - **Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.
    - Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned square** with **positive area**.

    An **axis-aligned square** is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

    Implement the `DetectSquares` class:

    - `DetectSquares()` Initializes the object with an empty data structure.
    - `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
    - `int count(int[] point)` Counts the number of ways to form **axis-aligned squares** with point `point = [x, y]` as described above.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/09/01/image.png)

    ```
    Input
    ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
    [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
    Output
    [null, null, null, null, 1, 0, null, 2]

    Explanation
    DetectSquares detectSquares = new DetectSquares();
    detectSquares.add([3, 10]);
    detectSquares.add([11, 2]);
    detectSquares.add([3, 2]);
    detectSquares.count([11, 10]); // return 1.
    detectSquares.count([14, 8]);  // return 0.
    detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
    detectSquares.count([11, 10]); // return 2.
    ```

    ## Constraints

    - `point.length == 2`
    - 0 <= x, y <= 1000
    - At most `3000` calls in total will be made to `add` and `count`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import Counter

    class DetectSquares:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def add(self, point: list[int]) -> None:
            raise NotImplementedError('Implement add')

        def count(self, point: list[int]) -> int:
            raise NotImplementedError('Implement count')

    practice_exports = {'Counter': Counter, 'DetectSquares': DetectSquares}
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
