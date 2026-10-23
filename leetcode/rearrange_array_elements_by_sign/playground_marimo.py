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
    # 2149. Rearrange Array Elements by Sign

    **Medium** · Array, Two Pointers, Simulation

    You are given a 0-indexed integer array `nums` of even length consisting of an equal number of positive and negative integers.

    You should return the array of nums such that the array follows the given conditions:

    1. Every consecutive pair of integers have opposite signs.
    2. For all integers with the same sign, the order in which they were present in nums is preserved.
    3. The rearranged array begins with a positive integer.

    Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

    ## Examples

    ```
    Input: nums = [3,1,-2,-5,2,-4]
    Output: [3,-2,1,-5,2,-4]
    ```
    **Explanation:** The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4]. The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].

    ```
    Input: nums = [-1,1]
    Output: [1,-1]
    ```
    **Explanation:** 1 is the only positive integer and -1 the only negative integer in nums. So nums is rearranged to [1,-1].

    ## Constraints

    - 2 <= nums.length <= 2 * 10^5
    - nums.length is even
    - 1 <= |nums[i]| <= 10^5
    - nums consists of equal number of positive and negative integers.

    It is not required to do the modifications in-place.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def rearrange_array(self, nums: list[int]) -> list[int]:
            raise NotImplementedError('Implement rearrange_array')

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
