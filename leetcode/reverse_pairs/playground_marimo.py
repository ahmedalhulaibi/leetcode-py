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
    # 493. Reverse Pairs

    **Hard** · Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap

    Given an integer array `nums`, return the number of **reverse pairs** in the array.

    A reverse pair is a pair `(i, j)` where:

    - `0 <= i < j < nums.length` and
    - `nums[i] > 2 * nums[j]`.

    ## Examples

    ```
    Input: nums = [1,3,2,3,1]
    Output: 2
    ```
    **Explanation:** The reverse pairs are:
    (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
    (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

    ```
    Input: nums = [2,4,3,5,1]
    Output: 3
    ```
    **Explanation:** The reverse pairs are:
    (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
    (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
    (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

    ## Constraints

    - 1 <= nums.length <= 5 * 10^4
    - -2^31 <= nums[i] <= 2^31 - 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def reverse_pairs(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement reverse_pairs')

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
