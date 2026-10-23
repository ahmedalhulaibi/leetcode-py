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
    # 1274. Number of Ships in a Rectangle

    **Hard** · Array, Divide and Conquer, Interactive

    (This problem is an **interactive problem**.)

    Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

    You have a function `Sea.has_ships(top_right, bottom_left)` which takes two points as arguments and returns `true` if there is at least one ship in the rectangle represented by the two points, including on the boundary.

    Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are **at most 10 ships** in that rectangle.

    Submissions making **more than 400 calls** to `has_ships` will be judged **Wrong Answer**. Also, any solutions that attempt to circumvent the judge will be disqualified.

    The API is:

    ```
    class Sea:
        def has_ships(self, top_right: 'Point', bottom_left: 'Point') -> bool: ...

    class Point:
        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y
    ```

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1274.Number%20of%20Ships%20in%20a%20Rectangle/images/1445_example_1.png)

    ```
    Input:
    ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
    Output: 3
    Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
    ```

    ```
    Input:
    ships = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
    Output: 3
    ```

    ## Constraints

    - On the input `ships` is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given `has_ships` API, without knowing the `ships` position.
    - `0 <= bottomLeft[0] <= topRight[0] <= 1000`
    - `0 <= bottomLeft[1] <= topRight[1] <= 1000`
    - `topRight != bottomLeft`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Point:

        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

    class Sea:

        def __init__(self, ships: list[list[int]]) -> None:
            self.ships = {(x, y) for x, y in ships}
            self.calls = 0

        def has_ships(self, top_right: Point, bottom_left: Point) -> bool:
            self.calls += 1
            if self.calls > 400:
                msg = 'has_ships exceeded the 400-call judge limit'
                raise RuntimeError(msg)
            return any((bottom_left.x <= x <= top_right.x and bottom_left.y <= y <= top_right.y for x, y in self.ships))

    class Solution:

        def count_ships(self, sea: Sea, top_right: Point, bottom_left: Point) -> int:
            raise NotImplementedError('Implement count_ships')

    practice_exports = {'Point': Point, 'Sea': Sea, 'Solution': Solution}
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
