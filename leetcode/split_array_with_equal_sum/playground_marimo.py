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
    # 548. Split Array with Equal Sum

    **Hard** · Array, Hash Table, Prefix Sum

    Given an integer array `nums` of length `n`, return `true` if there is a triplet `(i, j, k)` which satisfies the following conditions:

    - `0 < i, i + 1 < j, j + 1 < k < n - 1`
    - The sum of subarrays `(0, i - 1)`, `(i + 1, j - 1)`, `(j + 1, k - 1)` and `(k + 1, n - 1)` is equal.

    A subarray `(l, r)` represents a slice of the original array starting from the element indexed `l` to the element indexed `r`.

    ## Examples

    ```
    Input: nums = [1,2,1,2,1,2,1]
    Output: true
    Explanation:
    i = 1, j = 3, k = 5.
    sum(0, i - 1) = sum(0, 0) = 1
    sum(i + 1, j - 1) = sum(2, 2) = 1
    sum(j + 1, k - 1) = sum(4, 4) = 1
    sum(k + 1, n - 1) = sum(6, 6) = 1
    ```

    ```
    Input: nums = [1,2,1,2,1,2,1,2]
    Output: false
    ```

    ## Constraints

    - `n == nums.length`
    - `1 <= n <= 2000`
    - `-10^6 <= nums[i] <= 10^6`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def split_array(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement split_array')

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
