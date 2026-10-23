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
    # 446. Arithmetic Slices II - Subsequence

    **Hard** · Array, Dynamic Programming

    Given an integer array `nums`, return *the number of all the **arithmetic subsequences** of* `nums`.

    A sequence of numbers is called arithmetic if it consists of **at least three elements** and if the difference between any two consecutive elements is the same.

    - For example, `[1, 3, 5, 7, 9]`, `[7, 7, 7, 7]`, and `[3, -1, -5, -9]` are arithmetic sequences.
    - For example, `[1, 1, 2, 5, 7]` is not an arithmetic sequence.

    A **subsequence** of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

    - For example, `[2,5,10]` is a subsequence of `[1,2,1,**2**,4,1,**5**,**10**]`.

    The test cases are generated so that the answer fits in **32-bit** integer.

    ## Examples

    ```
    Input: nums = [2,4,6,8,10]
    Output: 7
    Explanation: All arithmetic subsequence slices are:
    [2,4,6]
    [4,6,8]
    [6,8,10]
    [2,4,6,8]
    [4,6,8,10]
    [2,4,6,8,10]
    [2,6,10]
    ```

    ```
    Input: nums = [7,7,7,7,7]
    Output: 16
    Explanation: Any subsequence of this array is arithmetic.
    ```

    ## Constraints

    - `1 <= nums.length <= 1000`
    - `-2^31 <= nums[i] <= 2^31 - 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def number_of_arithmetic_slices(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement number_of_arithmetic_slices')

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
