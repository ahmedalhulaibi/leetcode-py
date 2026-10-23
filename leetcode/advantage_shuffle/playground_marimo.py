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
    # 870. Advantage Shuffle

    **Medium** · Array, Two Pointers, Greedy, Sorting

    You are given two integer arrays `nums1` and `nums2` both of the same length. The **advantage** of `nums1` with respect to `nums2` is the number of indices `i` for which `nums1[i] > nums2[i]`.

    Return _any_ permutation of `nums1` that maximizes its **advantage** with respect to `nums2`.

    ## Examples

    ```
    Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
    Output: [2,11,7,15]
    ```

    ```
    Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
    Output: [24,32,8,12]
    ```

    ## Constraints

    - `1 <= nums1.length <= 10^5`
    - `nums2.length == nums1.length`
    - `0 <= nums1[i], nums2[i] <= 10^9`

    **Note:** Multiple permutations can achieve the maximum advantage, so any valid one is accepted. The tests assert that the result is a permutation of `nums1` that reaches the maximum possible advantage count.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def advantage_count(self, nums1: list[int], nums2: list[int]) -> list[int]:
            raise NotImplementedError('Implement advantage_count')

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
