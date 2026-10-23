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
    # 775. Global and Local Inversions

    **Medium** · Array, Math

    You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

    The number of global inversions is the number of the different pairs (i, j) where:

    - 0 <= i < j < n
    - nums[i] > nums[j]

    The number of local inversions is the number of indices i where:

    - 0 <= i < n - 1
    - nums[i] > nums[i + 1]

    Return `true` if the number of global inversions is equal to the number of local inversions.

    ## Examples

    ```
    Input: nums = [1,0,2]
    Output: true
    Explanation: There is 1 global inversion and 1 local inversion.
    ```

    ```
    Input: nums = [1,2,0]
    Output: false
    Explanation: There are 2 global inversions and 1 local inversion.
    ```

    ## Constraints

    - n == nums.length
    - 1 <= n <= 10^5
    - 0 <= nums[i] < n
    - All the integers of nums are unique.
    - nums is a permutation of all the numbers in the range [0, n - 1].



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_ideal_permutation(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement is_ideal_permutation')

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
