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
    # 1428. Leftmost Column with at Least a One

    **Medium** · Array, Binary Search, Interactive, Matrix

    A <strong>row-sorted binary matrix</strong> means that all elements are <code>0</code> or <code>1</code> and each row of the matrix is sorted in non-decreasing order.

    Given a <strong>row-sorted binary matrix</strong> <code>binaryMatrix</code>, return <em>the index (0-indexed) of the <strong>leftmost column</strong> with a 1 in it</em>. If such an index does not exist, return <code>-1</code>.

    <strong>You can't access the Binary Matrix directly.</strong> You may only access the matrix using a <code>BinaryMatrix</code> interface:

    <ul>
    <li><code>BinaryMatrix.get(row, col)</code> returns the element of the matrix at index <code>(row, col)</code> (0-indexed).</li>
    <li><code>BinaryMatrix.dimensions()</code> returns the dimensions of the matrix as a list of 2 elements <code>[rows, cols]</code>, which means the matrix is <code>rows x cols</code>.</li>
    </ul>

    Submissions making more than <code>1000</code> calls to <code>BinaryMatrix.get</code> will be judged <em>Wrong Answer</em>.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1428.Leftmost%20Column%20with%20at%20Least%20a%20One/images/untitled-diagram-5.jpg)

    ```
    Input: mat = [[0,0],[1,1]]
    Output: 0
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1428.Leftmost%20Column%20with%20at%20Least%20a%20One/images/untitled-diagram-4.jpg)

    ```
    Input: mat = [[0,0],[0,1]]
    Output: 1
    ```

    ![Example 3](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1428.Leftmost%20Column%20with%20at%20Least%20a%20One/images/untitled-diagram-3.jpg)

    ```
    Input: mat = [[0,0],[0,0]]
    Output: -1
    ```

    ## Constraints

    - <code>rows == mat.length</code>
    - <code>cols == mat[i].length</code>
    - <code>1 &lt;= rows, cols &lt;= 100</code>
    - <code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.
    - <code>mat[i]</code> is sorted in non-decreasing order.

    <strong>Follow up:</strong> Could you find a solution with a complexity better than <code>O(rows x cols)</code>?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class BinaryMatrix:

        def __init__(self, mat: list[list[int]]) -> None:
            self.mat = mat
            self.calls = 0

        def get(self, row: int, col: int) -> int:
            self.calls += 1
            return self.mat[row][col]

        def dimensions(self) -> list[int]:
            return [len(self.mat), len(self.mat[0])]

    class Solution:

        def leftmost_column_with_one(self, binary_matrix: BinaryMatrix) -> int:
            raise NotImplementedError('Implement leftmost_column_with_one')

    practice_exports = {'BinaryMatrix': BinaryMatrix, 'Solution': Solution}
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
