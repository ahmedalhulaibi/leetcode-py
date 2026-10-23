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
    # 1060. Missing Element in Sorted Array

    **Medium** · Array, Binary Search

    Given an integer array `nums` which is sorted in **ascending order** and all of its elements are **unique** and given also an integer `k`, return the `kth` missing number starting from the leftmost number of the array.

    ## Examples

    ```
    Input: nums = [4,7,9,10], k = 1
    Output: 5
    Explanation: The first missing number is 5.
    ```

    ```
    Input: nums = [4,7,9,10], k = 3
    Output: 8
    Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
    ```

    ```
    Input: nums = [1,2,4], k = 3
    Output: 6
    Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
    ```

    ## Constraints

    - 1 <= nums.length <= 5 * 10^4
    - 1 <= nums[i] <= 10^7
    - nums is sorted in ascending order, and all the elements are unique.
    - 1 <= k <= 10^8

    **Follow up:** Can you find a logarithmic time complexity (i.e., `O(log(n))`) solution?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def missing_element(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement missing_element')

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
