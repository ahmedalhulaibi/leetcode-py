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
    mo.md(r"""
    # 1508. Range Sum of Sorted Subarray Sums

    **Medium** · Array, Two Pointers, Binary Search, Sorting, Prefix Sum

    <p>You are given the array <code>nums</code> consisting of <code>n</code> positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of <code>n * (n + 1) / 2</code> numbers.</p>

    <p><em>Return the sum of the numbers from index </em><code>left</code><em> to index </em><code>right</code> (<strong>indexed from 1</strong>)<em>, inclusive, in the new array. </em>Since the answer can be a huge number return it modulo <code>10<sup>9</sup> + 7</code>.</p>

    ## Examples

    ```
    Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
    Output: 13
    Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.
    ```

    ```
    Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
    Output: 6
    Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
    ```

    ```
    Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
    Output: 50
    ```

    ## Constraints

    <ul>
        <li><code>n == nums.length</code></li>
        <li><code>1 &lt;= nums.length &lt;= 1000</code></li>
        <li><code>1 &lt;= nums[i] &lt;= 100</code></li>
        <li><code>1 &lt;= left &lt;= right &lt;= n * (n + 1) / 2</code></li>
    </ul>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
            raise NotImplementedError('Implement range_sum')

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
