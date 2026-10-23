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
    # 1985. Find the Kth Largest Integer in the Array

    **Medium** · Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect

    You are given an array of strings `nums` and an integer `k`. Each string in `nums` represents an integer without leading zeros.

    Return the string that represents the `kth` largest integer in `nums`.

    **Note**: Duplicate numbers should be counted distinctly. For example, if `nums` is `["1","2","2"]`, `"2"` is the first largest integer, `"2"` is the second-largest integer, and `"1"` is the third-largest integer.

    ## Examples

    ```
    Input: nums = ["3","6","7","10"], k = 4
    Output: "3"
    Explanation: The numbers in nums sorted in non-decreasing order are ["3","6","7","10"]. The 4th largest integer in nums is "3".
    ```

    ```
    Input: nums = ["2","21","12","1"], k = 3
    Output: "2"
    Explanation: The numbers in nums sorted in non-decreasing order are ["1","2","12","21"]. The 3rd largest integer in nums is "2".
    ```

    ```
    Input: nums = ["0","0"], k = 2
    Output: "0"
    Explanation: The numbers in nums sorted in non-decreasing order are ["0","0"]. The 2nd largest integer in nums is "0".
    ```

    ## Constraints

    - 1 <= k <= nums.length <= 10^4
    - 1 <= nums[i].length <= 100
    - nums[i] consists of only digits.
    - nums[i] will not have any leading zeros.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def kth_largest_number(self, nums: list[str], k: int) -> str:
            raise NotImplementedError('Implement kth_largest_number')

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
