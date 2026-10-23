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
    # 719. Find K-th Smallest Pair Distance

    **Hard** · Array, Two Pointers, Binary Search, Sorting

    The distance of a pair of integers `a` and `b` is defined as the absolute difference between `a` and `b`.

    Given an integer array `nums` and an integer `k`, return the `kth` smallest distance among all the pairs `nums[i]` and `nums[j]` where `0 <= i < j < nums.length`.

    ## Examples

    ```
    Input: nums = [1,3,1], k = 1
    Output: 0
    Explanation: Here are all the pairs:
    (1,3) -> 2
    (1,1) -> 0
    (3,1) -> 2
    Then the 1st smallest distance pair is (1,1), and its distance is 0.
    ```

    ```
    Input: nums = [1,1,1], k = 2
    Output: 0
    ```

    ```
    Input: nums = [1,6,1], k = 3
    Output: 5
    ```

    ## Constraints

    - n == nums.length
    - 2 <= n <= 10^4
    - 0 <= nums[i] <= 10^6
    - 1 <= k <= n * (n - 1) / 2



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from bisect import bisect_right

    class Solution:

        def smallest_distance_pair(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement smallest_distance_pair')

    practice_exports = {'bisect_right': bisect_right, 'Solution': Solution}
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
