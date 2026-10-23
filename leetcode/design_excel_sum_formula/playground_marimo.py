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
    # 631. Design Excel Sum Formula

    **Hard** · Graph, Design, Topological Sort, Array, Hash Table, String, Matrix

    Design the basic function of **Excel** and implement the function of the sum formula.

    Implement the `Excel` class:

    - `Excel(int height, char width)` Initializes the object with the `height` and the `width` of the sheet. The sheet is an integer matrix `mat` of size `height x width` with the row index in the range `[1, height]` and the column index in the range `['A', width]`. All the values should be **zero** initially.
    - `void set(int row, char column, int val)` Changes the value at `mat[row][column]` to be `val`.
    - `int get(int row, char column)` Returns the value at `mat[row][column]`.
    - `int sum(int row, char column, List<String> numbers)` Sets the value at `mat[row][column]` to be the sum of cells represented by `numbers` and returns the value at `mat[row][column]`. This sum formula **should exist** until this cell is overlapped by another value or another sum formula. `numbers[i]` could be on the format:
      - `"ColRow"` that represents a single cell. For example, `"F7"` represents the cell `mat[7]['F']`.
      - `"ColRow1:ColRow2"` that represents a range of cells. The range will always be a rectangle where `"ColRow1"` represents the position of the top-left cell, and `"ColRow2"` represents the position of the bottom-right cell.

    **Note:** You could assume that there will not be any circular sum reference.

    ## Examples

    ```
    Input
    ["Excel", "set", "sum", "set", "get"]
    [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
    Output
    [null, null, 4, null, 6]

    Explanation
    Excel excel = new Excel(3, "C");
    excel.set(1, "A", 2);
    excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
    excel.set(2, "B", 2);
    excel.get(3, "C"); // return 6
    ```

    ## Constraints

    - `1 <= height <= 26`
    - `'A' <= width <= 'Z'`
    - `1 <= row <= height`
    - `'A' <= column <= width`
    - `-100 <= val <= 100`
    - `1 <= numbers.length <= 5`
    - `numbers[i]` has the format `"ColRow"` or `"ColRow1:ColRow2"`.
    - At most `100` calls will be made to `set`, `get`, and `sum`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Excel:

        def __init__(self, height: int, width: str) -> None:
            raise NotImplementedError('Implement __init__')

        def set(self, row: int, column: str, val: int) -> None:
            raise NotImplementedError('Implement set')

        def get(self, row: int, column: str) -> int:
            raise NotImplementedError('Implement get')

        def sum(self, row: int, column: str, numbers: list[str]) -> int:
            raise NotImplementedError('Implement sum')

    practice_exports = {'Excel': Excel}
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
