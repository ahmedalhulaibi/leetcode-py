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
    # 1183. Maximum Number of Ones

    **Hard** · Math, Greedy, Sorting, Heap (Priority Queue)

    Consider a matrix `M` with dimensions `width * height`, such that every cell has value `0` or `1`, and any **square** sub-matrix of `M` of size `sideLength * sideLength` has at most `maxOnes` ones.

    Return the maximum possible number of ones that the matrix `M` can have.

    ## Examples

    ```
    Input: width = 3, height = 3, sideLength = 2, maxOnes = 1
    Output: 4
    ```
    **Explanation:**
    In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
    The best solution that has 4 ones is:
    [1,0,1]
    [0,0,0]
    [1,0,1]

    ```
    Input: width = 3, height = 3, sideLength = 2, maxOnes = 2
    Output: 6
    ```
    **Explanation:**
    [1,0,1]
    [1,0,1]
    [1,0,1]

    ## Constraints

    - 1 <= width, height <= 100
    - 1 <= sideLength <= width, height
    - 0 <= maxOnes <= sideLength * sideLength



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_number_of_ones(self, width: int, height: int, side_length: int, max_ones: int) -> int:
            raise NotImplementedError('Implement maximum_number_of_ones')

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
