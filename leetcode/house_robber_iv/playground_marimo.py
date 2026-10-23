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
    # 2560. House Robber IV

    **Medium** · Array, Binary Search, Dynamic Programming, Greedy

    There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he **refuses to steal from adjacent homes**.

    The **capability** of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

    You are given an integer array `nums` representing how much money is stashed in each house. More formally, the `i<sup>th</sup>` house from the left has `nums[i]` dollars.

    You are also given an integer `k`, representing the **minimum** number of houses the robber will steal from. It is always possible to steal at least `k` houses.

    Return *the **minimum** capability of the robber out of all the possible ways to steal at least* `k` *houses*.

    ## Examples

    ```
    Input: nums = [2,3,5,9], k = 2
    Output: 5
    ```
    **Explanation:** There are three ways to rob at least 2 houses:
    - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
    - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
    - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
    Therefore, we return min(5, 9, 9) = 5.

    ```
    Input: nums = [2,7,9,3,1], k = 2
    Output: 2
    ```
    **Explanation:** There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.

    ## Constraints

    - 1 <= nums.length <= 10<sup>5</sup>
    - 1 <= nums[i] <= 10<sup>9</sup>
    - 1 <= k <= (nums.length + 1)/2



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_capability(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement min_capability')

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
