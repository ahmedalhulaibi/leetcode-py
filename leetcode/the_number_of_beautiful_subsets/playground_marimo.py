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
    # 2597. The Number of Beautiful Subsets

    **Medium** · Array, Hash Table, Math, Dynamic Programming, Backtracking, Sorting, Combinatorics

    You are given an array `nums` of positive integers and a **positive** integer `k`.

    A subset of `nums` is **beautiful** if it does not contain two integers with an absolute difference equal to `k`.

    Return *the number of **non-empty beautiful** subsets of the array* `nums`.

    A **subset** of `nums` is an array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

    ## Examples

    ```
    Input: nums = [2,4,6], k = 2
    Output: 4
    ```
    **Explanation:** The beautiful subsets of the array nums are: `[2]`, `[4]`, `[6]`, `[2, 6]`. It can be proved that there are only 4 beautiful subsets in the array `[2,4,6]`.

    ```
    Input: nums = [1], k = 1
    Output: 1
    ```
    **Explanation:** The beautiful subset of the array nums is `[1]`. It can be proved that there is only 1 beautiful subset in the array `[1]`.

    ## Constraints

    - `1 <= nums.length <= 18`
    - `1 <= nums[i], k <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def beautiful_subsets(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement beautiful_subsets')

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
