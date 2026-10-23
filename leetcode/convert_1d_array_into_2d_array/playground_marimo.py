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
    # 2022. Convert 1D Array Into 2D Array

    **Easy** · Array, Matrix, Simulation

    You are given a 0-indexed 1-dimensional (1D) integer array `original`, and two integers, `m` and `n`. You are tasked with creating a 2-dimensional (2D) array with  `m` rows and `n` columns using **all** the elements from `original`.

    The elements from indices `0` to `n - 1` (**inclusive**) of `original` should form the first row of the constructed 2D array, the elements from indices `n` to `2 * n - 1` (**inclusive**) should form the second row of the constructed 2D array, and so on.

    Return *an* `m x n` *2D array constructed according to the above procedure, or an empty 2D array if it is impossible*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/08/26/image-20210826114243-1.png)

    ```
    Input: original = [1,2,3,4], m = 2, n = 2
    Output: [[1,2],[3,4]]
    Explanation: The constructed 2D array should contain 2 rows and 2 columns.
    The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
    The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
    ```

    ```
    Input: original = [1,2,3], m = 1, n = 3
    Output: [[1,2,3]]
    Explanation: The constructed 2D array should contain 1 row and 3 columns.
    Put all three elements in original into the first row of the constructed 2D array.
    ```

    ```
    Input: original = [1,2], m = 1, n = 1
    Output: []
    Explanation: There are 2 elements in original.
    It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
    ```

    ## Constraints

    - `1 <= original.length <= 5 * 10^4`
    - `1 <= original[i] <= 10^5`
    - `1 <= m, n <= 4 * 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def construct_2d_array(self, original: list[int], m: int, n: int) -> list[list[int]]:
            raise NotImplementedError('Implement construct_2d_array')

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
