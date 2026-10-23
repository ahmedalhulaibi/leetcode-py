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
    # 378. Kth Smallest Element in a Sorted Matrix

    **Medium** · Array, Binary Search, Sorting, Heap (Priority Queue), Matrix

    Given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    You must find a solution with a memory complexity better than O(n2).

    ## Examples

    ```
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
    ```

    ```
    Input: matrix = [[-5]], k = 1
    Output: -5
    ```

    ## Constraints

    - n == matrix.length == matrix[i].length
    - 1 <= n <= 300
    - -10^9 <= matrix[i][j] <= 10^9
    - All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    - 1 <= k <= n2

    **Follow up:**

    - Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
    - Could you solve the problem in O(n) time complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def kth_smallest(self, matrix: list[list[int]], k: int) -> int:
            raise NotImplementedError('Implement kth_smallest')

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
