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
    # 1760. Minimum Limit of Balls in a Bag

    **Medium** · Array, Binary Search

    You are given an integer array `nums` where the `i<sup>th</sup>` bag contains `nums[i]` balls. You are also given an integer `maxOperations`.

    You can perform the following operation at most `maxOperations` times:

    - Take any bag of balls and divide it into two new bags with a **positive** number of balls.

      - For example, a bag of `5` balls can become two new bags of `1` and `4` balls, or two new bags of `2` and `3` balls.

    Your penalty is the **maximum** number of balls in a bag. You want to **minimize** your penalty after the operations.

    Return _the minimum possible penalty after performing the operations_.

    ## Examples

    ```
    Input: nums = [9], maxOperations = 2
    Output: 3
    Explanation:
    - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
    - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
    The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
    ```

    ```
    Input: nums = [2,4,8,2], maxOperations = 4
    Output: 2
    Explanation:
    - Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
    - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
    - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
    - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
    The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.
    ```

    ## Constraints

    - 1 <= nums.length <= 10<sup>5</sup>
    - 1 <= maxOperations, nums[i] <= 10<sup>9</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_size(self, nums: list[int], max_operations: int) -> int:
            raise NotImplementedError('Implement minimum_size')

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
