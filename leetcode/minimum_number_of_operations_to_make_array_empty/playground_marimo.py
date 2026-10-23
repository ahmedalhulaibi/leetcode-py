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
    # 2870. Minimum Number of Operations to Make Array Empty

    **Medium** · Array, Hash Table, Greedy, Counting

    <p>You are given a <strong>0-indexed</strong> array <code>nums</code> consisting of positive integers.</p>

    <p>There are two types of operations that you can apply on the array <strong>any</strong> number of times:</p>

    <ul>
        <li>Choose <strong>two</strong> elements with <strong>equal</strong> values and <strong>delete</strong> them from the array.</li>
        <li>Choose <strong>three</strong> elements with <strong>equal</strong> values and <strong>delete</strong> them from the array.</li>
    </ul>

    <p>Return <em>the <strong>minimum</strong> number of operations required to make the array empty, or </em><code>-1</code><em> if it is not possible</em>.</p>

    ## Examples

    ```
    Input: nums = [2,3,3,2,2,4,2,3,4]
    Output: 4
    Explanation: We can apply the following operations to make the array empty:
    - Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
    - Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
    - Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
    - Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
    It can be shown that we cannot make the array empty in less than 4 operations.
    ```

    ```
    Input: nums = [2,1,2,2,3,3]
    Output: -1
    Explanation: It is impossible to empty the array.
    ```

    ## Constraints

    - 2 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^6

    **Note:** This question is the same as 2244: Minimum Rounds to Complete All Tasks.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_operations(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement min_operations')

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
