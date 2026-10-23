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
    # 1425. Constrained Subsequence Sum

    **Hard** · Array, Dynamic Programming, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue

    Given an integer array <code>nums</code> and an integer <code>k</code>, return the maximum sum of a <strong>non-empty</strong> subsequence of that array such that for every two <strong>consecutive</strong> integers in the subsequence, <code>nums[i]</code> and <code>nums[j]</code>, where <code>i &lt; j</code>, the condition <code>j - i &lt;= k</code> is satisfied.</p>

    <p>A <em>subsequence</em> of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

    ## Examples

    ```
    Input: nums = [10,2,-10,5,20], k = 2
    Output: 37
    Explanation: The subsequence is [10, 2, 5, 20].
    ```

    ```
    Input: nums = [-1,-2,-3], k = 1
    Output: -1
    Explanation: The subsequence must be non-empty, so we choose the largest number.
    ```

    ```
    Input: nums = [10,-2,-10,-5,20], k = 2
    Output: 23
    Explanation: The subsequence is [10, -2, -5, 20].
    ```

    ## Constraints

    - 1 <= k <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class Solution:

        def constrained_subset_sum(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement constrained_subset_sum')

    practice_exports = {'deque': deque, 'Solution': Solution}
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
