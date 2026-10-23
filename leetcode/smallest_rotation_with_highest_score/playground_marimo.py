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
    # 798. Smallest Rotation with Highest Score

    **Hard** · Array, Prefix Sum

    You are given an array `nums`. You can rotate it by a non-negative integer `k` so that the array becomes `[nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]`. Afterward, any entries that are less than or equal to their index are worth one point.

    For example, if we have `nums = [2,4,1,3,0]`, and we rotate by `k = 2`, it becomes `[1,3,0,2,4]`. This is worth `3` points because `1 > 0` [no points], `3 > 1` [no points], `0 <= 2` [one point], `2 <= 3` [one point], `4 <= 4` [one point].

    Return *the rotation index* `k` *that corresponds to the highest score we can achieve if we rotated* `nums` *by it*. If there are multiple answers, return the smallest such index `k`.

    ## Examples

    ```
    Input: nums = [2,3,1,4,0]
    Output: 3
    ```
    **Explanation:** Scores for each k are listed below:
    k = 0,  nums = [2,3,1,4,0],    score 2
    k = 1,  nums = [3,1,4,0,2],    score 3
    k = 2,  nums = [1,4,0,2,3],    score 3
    k = 3,  nums = [4,0,2,3,1],    score 4
    k = 4,  nums = [0,2,3,1,4],    score 3
    So we should choose k = 3, which has the highest score.

    ```
    Input: nums = [1,3,0,2,4]
    Output: 0
    ```
    **Explanation:** nums will always have 3 points no matter how it shifts.
    So we will choose the smallest k, which is 0.

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `0 <= nums[i] < nums.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def best_rotation(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement best_rotation')

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
