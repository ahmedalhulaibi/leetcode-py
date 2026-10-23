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
    # 287. Find the Duplicate Number

    **Medium** · Array, Two Pointers, Binary Search, Bit Manipulation

    Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

    There is only **one repeated number** in `nums`, return *this repeated number*.

    You must solve the problem **without** modifying the array `nums` and using only constant extra space.

    ## Examples

    ```
    Input: nums = [1,3,4,2,2]
    Output: 2
    ```

    ```
    Input: nums = [3,1,3,4,2]
    Output: 3
    ```

    ```
    Input: nums = [3,3,3,3,3]
    Output: 3
    ```

    ## Constraints

    - `1 <= n <= 10^5`
    - `nums.length == n + 1`
    - `1 <= nums[i] <= n`
    - All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

    **Follow up:**

    - How can we prove that at least one duplicate number must exist in `nums`?
    - Can you solve the problem in linear runtime complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_duplicate(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement find_duplicate')

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
