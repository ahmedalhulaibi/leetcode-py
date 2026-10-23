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
    # 659. Split Array into Consecutive Subsequences

    **Medium** · Array, Hash Table, Greedy, Heap (Priority Queue)

    You are given an integer array `nums` that is sorted in non-decreasing order.

    Determine if it is possible to split `nums` into one or more subsequences such that both of the following conditions are true:

    - Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
    - All subsequences have a length of `3` or more.

    Return `true` if you can split `nums` according to the above conditions, or `false` otherwise.

    A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., `[1,3,5]` is a subsequence of `[1,2,3,4,5]` while `[1,3,2]` is not).

    ## Examples

    ```
    Input: nums = [1,2,3,3,4,5]
    Output: true
    Explanation: nums can be split into the following subsequences:
    [1,2,3,3,4,5] --> 1, 2, 3
    [1,2,3,3,4,5] --> 3, 4, 5
    ```

    ```
    Input: nums = [1,2,3,3,4,4,5,5]
    Output: true
    Explanation: nums can be split into the following subsequences:
    [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
    [1,2,3,3,4,4,5,5] --> 3, 4, 5
    ```

    ```
    Input: nums = [1,2,3,4,4,5]
    Output: false
    Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
    ```

    ## Constraints

    - `1 <= nums.length <= 10^4`
    - `-1000 <= nums[i] <= 1000`
    - `nums` is sorted in non-decreasing order.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_possible(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement is_possible')

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
