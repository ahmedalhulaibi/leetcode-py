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
    # 3191. Minimum Operations to Make Binary Array Elements Equal to One I

    **Medium** · Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum

    You are given a <span data-keyword="binary-array">binary array</span> `nums`.

    You can do the following operation on the array **any** number of times (possibly zero):

    - Choose **any** 3 **consecutive** elements from the array and **flip** **all** of them.

    Flipping an element means changing its value from 0 to 1, and from 1 to 0.

    Return the **minimum** number of operations required to make all elements in `nums` equal to 1. If it is impossible, return -1.

    ## Examples

    ```
    Input: nums = [0,1,1,1,0,0]
    Output: 3
    Explanation:
    We can do the following operations:
    - Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
    - Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
    - Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
    ```

    ```
    Input: nums = [0,1,1,1]
    Output: -1
    Explanation:
    It is impossible to make all elements equal to 1.
    ```

    ## Constraints

    - 3 <= nums.length <= 10^5
    - 0 <= nums[i] <= 1



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
