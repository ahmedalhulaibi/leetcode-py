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
    # 169. Majority Element

    **Easy** · Array, Hash Table, Divide and Conquer, Sorting, Counting

    Given an array `nums` of size `n`, return the majority element.

    The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

    ## Examples

    ```
    Input: nums = [3,2,3]
    Output: 3
    ```

    ```
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    ```

    ## Constraints

    - n == nums.length
    - 1 <= n <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9

    **Follow-up:** Could you solve the problem in linear time and in O(1) space?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def majority_element(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement majority_element')

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
