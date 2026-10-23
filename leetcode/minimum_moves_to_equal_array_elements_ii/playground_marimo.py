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
    # 462. Minimum Moves to Equal Array Elements II

    **Medium** · Array, Math, Sorting

    Given an integer array `nums` of size `n`, return *the minimum number of moves required to make all array elements equal*.

    In one move, you can increment or decrement an element of the array by `1`.

    Test cases are designed so that the answer will fit in a **32-bit** integer.

    ## Examples

    ```
    Input: nums = [1,2,3]
    Output: 2
    Explanation: Only two moves are needed (remember each move increments or decrements one element):
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
    ```

    ```
    Input: nums = [1,10,2,9]
    Output: 16
    ```

    ## Constraints

    - n == nums.length
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - The answer is guaranteed to fit in a 32-bit integer.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_moves2(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement min_moves2')

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
