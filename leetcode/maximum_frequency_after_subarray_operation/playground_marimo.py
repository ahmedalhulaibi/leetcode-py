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
    # 3434. Maximum Frequency After Subarray Operation

    **Medium** · Array, Hash Table, Dynamic Programming, Greedy, Enumeration, Prefix Sum

    You are given an array `nums` of length `n`. You are also given an integer `k`.

    You perform the following operation on `nums` **once**:

    - Select a subarray `nums[i..j]` where `0 <= i <= j <= n - 1`.
    - Select an integer `x` and add `x` to **all** the elements in `nums[i..j]`.

    Find the **maximum** frequency of the value `k` after the operation.

    ## Examples

    ```
    Input: nums = [1,2,3,4,5,6], k = 1
    Output: 2
    ```
    **Explanation:** After adding -5 to `nums[2..5]`, 1 has a frequency of 2 in `[1, 2, -2, -1, 0, 1]`.

    ```
    Input: nums = [10,2,3,4,5,5,4,3,2,2], k = 10
    Output: 4
    ```
    **Explanation:** After adding 8 to `nums[1..9]`, 10 has a frequency of 4 in `[10, 10, 11, 12, 13, 13, 12, 11, 10, 10]`.

    ## Constraints

    - 1 <= n == nums.length <= 10^5
    - 1 <= nums[i] <= 50
    - 1 <= k <= 50



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_frequency(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_frequency')

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
