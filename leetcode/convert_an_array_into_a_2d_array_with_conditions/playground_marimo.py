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
    # 2610. Convert an Array Into a 2D Array With Conditions

    **Medium** · Array, Hash Table

    You are given an integer array `nums`. You need to create a 2D array from `nums` satisfying the following conditions:

    - The 2D array should contain **only** the elements of the array `nums`.
    - Each row in the 2D array contains **distinct** integers.
    - The number of rows in the 2D array should be **minimal**.

    Return *the resulting array*. If there are multiple answers, return **any** of them.

    **Note** that the 2D array can have a different number of elements on each row.

    ## Examples

    ```
    Input: nums = [1,3,4,1,2,3,1]
    Output: [[1,3,4,2],[1,3],[1]]
    Explanation: We can create a 2D array that contains the following rows:
    - 1,3,4,2
    - 1,3
    - 1
    All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
    It can be shown that we cannot have less than 3 rows in a valid array.
    ```

    ```
    Input: nums = [1,2,3,4]
    Output: [[4,3,2,1]]
    Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
    ```

    ## Constraints

    - `1 <= nums.length <= 200`
    - `1 <= nums[i] <= nums.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_matrix(self, nums: list[int]) -> list[list[int]]:
            raise NotImplementedError('Implement find_matrix')

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
