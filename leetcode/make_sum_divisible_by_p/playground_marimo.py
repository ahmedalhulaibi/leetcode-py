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
    # 1590. Make Sum Divisible by P

    **Medium** · Array, Hash Table, Prefix Sum

    Given an array of positive integers <code>nums</code>, remove the <strong>smallest</strong> subarray (possibly <strong>empty</strong>) such that the <strong>sum</strong> of the remaining elements is divisible by <code>p</code>. It is <strong>not</strong> allowed to remove the whole array.</p>

    <p>Return <em>the length of the smallest subarray that you need to remove, or </em><code>-1</code><em> if it's impossible</em>.</p>

    <p>A <strong>subarray</strong> is defined as a contiguous block of elements in the array.</p>

    ## Examples

    ```
    Input: nums = [3,1,4,2], p = 6
    Output: 1
    Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
    ```

    ```
    Input: nums = [6,3,5,2], p = 9
    Output: 2
    Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
    ```

    ```
    Input: nums = [1,2,3], p = 3
    Output: 0
    Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
    ```

    ## Constraints

    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9
    - 1 <= p <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_subarray(self, nums: list[int], p: int) -> int:
            raise NotImplementedError('Implement min_subarray')

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
