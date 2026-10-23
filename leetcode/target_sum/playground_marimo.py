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
    # 494. Target Sum

    **Medium** · Array, Dynamic Programming, Backtracking

    You are given an integer array `nums` and an integer `target`.

    You want to build an expression out of nums by adding one of the symbols `+` and `-` before each integer in nums and then concatenate all the integers.

    - For example, if `nums = [2, 1]`, you can add a `+` before `2` and a `-` before `1` and concatenate them to build the expression `+2-1`.

    Return *the number of different expressions that you can build, which evaluates to* `target`.

    ## Examples

    ```
    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    ```
    **Explanation:** There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3

    ```
    Input: nums = [1], target = 1
    Output: 1
    ```

    ## Constraints

    - 1 <= nums.length <= 20
    - 0 <= nums[i] <= 1000
    - 0 <= sum(nums[i]) <= 1000
    - -1000 <= target <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_target_sum_ways(self, nums: list[int], target: int) -> int:
            raise NotImplementedError('Implement find_target_sum_ways')

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
