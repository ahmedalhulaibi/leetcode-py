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
    # 2601. Prime Subtraction Operation

    **Medium** · Array, Math, Binary Search, Greedy, Number Theory

    You are given a **0-indexed** integer array `nums` of length `n`.

    You can perform the following operation as many times as you want:

    - Pick an index `i` that you haven't picked before, and pick a prime `p` **strictly less than** `nums[i]`, then subtract `p` from `nums[i]`.

    Return *true if you can make `nums` a strictly increasing array using the above operation and false otherwise.*

    A **strictly increasing array** is an array whose each element is strictly greater than its preceding element.

    ## Examples

    ```
    Input: nums = [4,9,6,10]
    Output: true
    Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
    In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
    After the second operation, nums is sorted in strictly increasing order, so the answer is true.
    ```

    ```
    Input: nums = [6,8,11,12]
    Output: true
    Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
    ```

    ```
    Input: nums = [5,8,3]
    Output: false
    Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
    ```

    ## Constraints

    - `1 <= nums.length <= 1000`
    - `1 <= nums[i] <= 1000`
    - `nums.length == n`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def prime_sub_operation(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement prime_sub_operation')

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
