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
    # 908. Smallest Range I

    **Easy** · Array, Math

    You are given an integer array `nums` and an integer `k`.

    In one operation, you can choose any index `i` where `0 <= i < nums.length` and change `nums[i]` to `nums[i] + x` where `x` is an integer from the range `[-k, k]`. You can apply this operation **at most once** for each index `i`.

    The **score** of `nums` is the difference between the maximum and minimum elements in `nums`.

    Return *the minimum **score** of* `nums` *after applying the mentioned operation at most once for each index in it*.

    ## Examples

    ```
    Input: nums = [1], k = 0
    Output: 0
    Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
    ```

    ```
    Input: nums = [0,10], k = 2
    Output: 6
    Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
    ```

    ```
    Input: nums = [1,3,6], k = 3
    Output: 0
    Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
    ```

    ## Constraints

    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 10^4
    - 0 <= k <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def smallest_range_i(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement smallest_range_i')

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
