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
    # 321. Create Maximum Number

    **Hard** · Array, Two Pointers, Stack, Greedy, Monotonic Stack

    You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` respectively. `nums1` and `nums2` represent the digits of two numbers. You are also given an integer `k`.

    Create the maximum number of length `k <= m + n` from digits of the two numbers. The relative order of the digits from the same array must be preserved.

    Return an array of the `k` digits representing the answer.

    ## Examples

    ```
    Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
    Output: [9,8,6,5,3]
    ```

    ```
    Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
    Output: [6,7,6,0,4]
    ```

    ```
    Input: nums1 = [3,9], nums2 = [8,9], k = 3
    Output: [9,8,9]
    ```

    ## Constraints

    - `m == nums1.length`
    - `n == nums2.length`
    - `1 <= m, n <= 500`
    - `0 <= nums1[i], nums2[i] <= 9`
    - `1 <= k <= m + n`
    - `nums1` and `nums2` do not have leading zeros.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_number(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
            raise NotImplementedError('Implement max_number')

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
