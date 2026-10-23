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
    # 308. Range Sum Query 2D - Mutable

    **Medium** · Design, Binary Indexed Tree, Segment Tree, Array, Matrix

    Given a 2D matrix `matrix`, handle multiple queries of the following types:

    1. **Update** the value of a cell in `matrix`.
    2. Calculate the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

    Implement the `NumMatrix` class:

    - `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.
    - `void update(int row, int col, int val)` **Updates** the value of `matrix[row][col]` to be `val`.
    - `int sumRegion(int row1, int col1, int row2, int col2)` Returns the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0308.Range%20Sum%20Query%202D%20-%20Mutable/images/summut-grid.jpg)

    ```
    Input
    ["NumMatrix", "sumRegion", "update", "sumRegion"]
    [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
    Output
    [null, 8, null, 10]

    Explanation
    NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
    numMatrix.sumRegion(2, 1, 4, 3); // return 8
    numMatrix.update(3, 2, 2); // matrix changes from left image to right image
    numMatrix.sumRegion(2, 1, 4, 3); // return 10
    ```

    ## Constraints

    - `m == matrix.length`
    - `n == matrix[i].length`
    - `1 <= m, n <= 200`
    - `-1000 <= matrix[i][j] <= 1000`
    - `0 <= row < m`
    - `0 <= col < n`
    - `-1000 <= val <= 1000`
    - `0 <= row1 <= row2 < m`
    - `0 <= col1 <= col2 < n`
    - At most `5000` calls will be made to `sumRegion` and `update`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class BinaryIndexedTree:

        def __init__(self, n: int) -> None:
            self.n = n
            self.c = [0] * (n + 1)

        @staticmethod
        def lowbit(x: int) -> int:
            return x & -x

        def update(self, x: int, delta: int) -> None:
            while x <= self.n:
                self.c[x] += delta
                x += BinaryIndexedTree.lowbit(x)

        def query(self, x: int) -> int:
            s = 0
            while x > 0:
                s += self.c[x]
                x -= BinaryIndexedTree.lowbit(x)
            return s

    class NumMatrix:

        def __init__(self, matrix: list[list[int]]) -> None:
            raise NotImplementedError('Implement __init__')

        def update(self, row: int, col: int, val: int) -> None:
            raise NotImplementedError('Implement update')

        def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
            raise NotImplementedError('Implement sum_region')

    practice_exports = {'BinaryIndexedTree': BinaryIndexedTree, 'NumMatrix': NumMatrix}
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
