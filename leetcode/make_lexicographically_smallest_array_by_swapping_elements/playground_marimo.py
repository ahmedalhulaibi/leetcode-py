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
    # 2948. Make Lexicographically Smallest Array by Swapping Elements

    **Medium** · Array, Union-Find, Sorting

    You are given a 0-indexed array of positive integers `nums` and a positive integer `limit`.

    In one operation, you can choose any two indices `i` and `j` and swap `nums[i]` and `nums[j]` **if** `|nums[i] - nums[j]| <= limit`.

    Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

    An array `a` is lexicographically smaller than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is less than the corresponding element in `b`. For example, the array `[2,10,3]` is lexicographically smaller than the array `[10,2,3]` because they differ at index `0` and `2 < 10`.

    ## Examples

    ```
    Input: nums = [1,5,3,9,8], limit = 2
    Output: [1,3,5,8,9]
    Explanation: Apply the operation 2 times:
    - Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
    - Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
    We cannot obtain a lexicographically smaller array by applying any more operations.
    Note that it may be possible to get the same result by doing different operations.
    ```

    ```
    Input: nums = [1,7,6,18,2,1], limit = 3
    Output: [1,6,7,18,1,2]
    Explanation: Apply the operation 3 times:
    - Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
    - Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
    - Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
    We cannot obtain a lexicographically smaller array by applying any more operations.
    ```

    ```
    Input: nums = [1,7,28,19,10], limit = 3
    Output: [1,7,28,19,10]
    Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
    ```

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `1 <= nums[i] <= 10^9`
    - `1 <= limit <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def lexicographically_smallest_array(self, nums: list[int], limit: int) -> list[int]:
            raise NotImplementedError('Implement lexicographically_smallest_array')

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
