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
    # 2530. Maximal Score After Applying K Operations

    **Medium** · Array, Greedy, Heap (Priority Queue)

    You are given a 0-indexed integer array `nums` and an integer `k`. You have a starting score of 0.

    In one operation:

    - choose an index `i` such that `0 <= i < nums.length`,
    - increase your score by `nums[i]`, and
    - replace `nums[i]` with `ceil(nums[i] / 3)`.

    Return the maximum possible score you can attain after applying exactly `k` operations.

    The ceiling function `ceil(val)` is the least integer greater than or equal to `val`.

    ## Examples

    ```
    Input: nums = [10,10,10,10,10], k = 5
    Output: 50
    Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
    ```

    ```
    Input: nums = [1,10,3,3,3], k = 3
    Output: 17
    Explanation: You can do the following operations:
    Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
    Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
    Operation 3: Select i = 2, so nums becomes [1,2,1,3,3]. Your score increases by 3.
    The final score is 10 + 4 + 3 = 17.
    ```

    ## Constraints

    - 1 <= nums.length, k <= 10^5
    - 1 <= nums[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_kelements(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_kelements')

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
