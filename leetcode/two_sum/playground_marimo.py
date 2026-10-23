# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.25.2",
#     "leetcode-py-sdk[practice]==0.0.0",
# ]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def imports():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def statement(mo):
    mo.md("""
    # 1. Two Sum

    **Easy** · Array, Hash Table

    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    ## Examples

    ```
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    ```
    **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

    ```
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    ```

    ```
    Input: nums = [3,3], target = 6
    Output: [0,1]
    ```

    ## Constraints

    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.

    **Follow-up:** Can you come up with an algorithm that is less than O(n^2) time complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def your_solution():
    class Solution:

        def two_sum(self, nums: list[int], target: int) -> list[int]:
            raise NotImplementedError('Implement two_sum')

    practice_exports = {'Solution': Solution}
    return (practice_exports,)


@app.cell(hide_code=True)
def test_button(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def test_results(mo, practice_exports, run_practice_tests, run_tests):
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
def notes(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
