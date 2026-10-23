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
    # 1671. Minimum Number of Removals to Make Mountain Array

    **Hard** · Array, Binary Search, Dynamic Programming, Greedy

    You may recall that an array `arr` is a **mountain array** if and only if:

    - `arr.length >= 3`
    - There exists some index `i` (**0-indexed**) with `0 < i < arr.length - 1` such that:
      - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
      - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

    Given an integer array `nums`, return the minimum number of elements to remove to make `nums` a mountain array.

    ## Examples

    ```
    Input: nums = [1,3,1]
    Output: 0
    Explanation: The array itself is a mountain array so we do not need to remove any elements.
    ```

    ```
    Input: nums = [2,1,1,5,6,2,3,1]
    Output: 3
    Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
    ```

    ## Constraints

    - `3 <= nums.length <= 1000`
    - `1 <= nums[i] <= 10^9`
    - It is guaranteed that you can make a mountain array out of `nums`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_mountain_removals(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement minimum_mountain_removals')

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
