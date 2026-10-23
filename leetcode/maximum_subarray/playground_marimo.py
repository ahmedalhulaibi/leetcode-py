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
    # 53. Maximum Subarray

    **Medium** · Array, Divide and Conquer, Dynamic Programming

    Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

    ## Examples

    ```
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    ```
    **Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

    ```
    Input: nums = [1]
    Output: 1
    ```
    **Explanation:** The subarray [1] has the largest sum 1.

    ```
    Input: nums = [5,4,-1,7,8]
    Output: 23
    ```
    **Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `-10^4 <= nums[i] <= 10^4`

    **Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_sub_array(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement max_sub_array')

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
