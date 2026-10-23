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
    # 480. Sliding Window Median

    **Hard** · Array, Hash Table, Sliding Window, Heap (Priority Queue), Treap

    The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

    - For examples, if `arr = [2,**3**,4]`, the median is `3`.
    - For examples, if `arr = [1,**2,3**,4]`, the median is `(2 + 3) / 2 = 2.5`.

    You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

    Return *the median array for each window in the original array*. Answers within `10^-5` of the actual value will be accepted.

    ## Examples

    ```
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
    ```
    **Explanation:**

    Window position                Median
    ---------------                -----
    [1  3  -1] -3  5  3  6  7        1
     1 [3  -1  -3] 5  3  6  7       -1
     1  3 [-1  -3  5] 3  6  7       -1
     1  3  -1 [-3  5  3] 6  7        3
     1  3  -1  -3 [5  3  6] 7        5
     1  3  -1  -3  5 [3  6  7]       6

    ```
    Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
    Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
    ```

    ## Constraints

    - 1 <= k <= nums.length <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import heapq

    class Solution:

        def median_sliding_window(self, nums: list[int], k: int) -> list[float]:
            raise NotImplementedError('Implement median_sliding_window')

    practice_exports = {'heapq': heapq, 'Solution': Solution}
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
