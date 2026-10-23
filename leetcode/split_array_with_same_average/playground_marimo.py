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
    # 805. Split Array With Same Average

    **Hard** · Array, Dynamic Programming, Bit Manipulation, Bitmask

    You are given an integer array `nums`.

    You should move each element of `nums` into one of the two arrays `A` and `B` such that `A` and `B` are non-empty, and `average(A) == average(B)`.

    Return `true` if it is possible to achieve that and `false` otherwise.

    **Note** that for an array `arr`, `average(arr)` is the sum of all the elements of `arr` over the length of `arr`.

    ## Examples

    ```
    Input: nums = [1,2,3,4,5,6,7,8]
    Output: true
    Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
    ```

    ```
    Input: nums = [3,1]
    Output: false
    ```

    ## Constraints

    - 1 <= nums.length <= 30
    - 0 <= nums[i] <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def split_array_same_average(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement split_array_same_average')

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
