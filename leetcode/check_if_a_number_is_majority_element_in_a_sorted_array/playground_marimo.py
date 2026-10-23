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
    # 1150. Check If a Number Is Majority Element in a Sorted Array

    **Easy** · Array, Binary Search

    Given an integer array `nums` sorted in non-decreasing order and an integer `target`, return `true` if `target` is a **majority** element, or `false` otherwise.

    A **majority** element in an array `nums` is an element that appears more than `nums.length / 2` times in the array.

    ## Examples

    ```
    Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
    Output: true
    ```
    **Explanation:** The value 5 appears 5 times and the length of the array is 9. Thus, 5 is a majority element because 5 > 9/2 is true.

    ```
    Input: nums = [10,100,101,101], target = 101
    Output: false
    ```
    **Explanation:** The value 101 appears 2 times and the length of the array is 4. Thus, 101 is not a majority element because 2 > 4/2 is false.

    ## Constraints

    - `1 <= nums.length <= 1000`
    - `1 <= nums[i], target <= 10^9`
    - `nums` is sorted in non-decreasing order.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_majority_element(self, nums: list[int], target: int) -> bool:
            raise NotImplementedError('Implement is_majority_element')

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
