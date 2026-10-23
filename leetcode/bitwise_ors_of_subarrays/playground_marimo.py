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
    # 898. Bitwise ORs of Subarrays

    **Medium** · Array, Dynamic Programming, Bit Manipulation

    Given an integer array `arr`, return *the number of distinct bitwise ORs of all the non-empty subarrays of* `arr`.

    The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

    A **subarray** is a contiguous non-empty sequence of elements within an array.

    ## Examples

    ```
    Input: arr = [0]
    Output: 1
    Explanation: There is only one possible result: 0.
    ```

    ```
    Input: arr = [1,1,2]
    Output: 3
    Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
    These yield the results 1, 1, 2, 1, 3, 3.
    There are 3 unique values, so the answer is 3.
    ```

    ```
    Input: arr = [1,2,4]
    Output: 6
    Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
    ```

    ## Constraints

    - `1 <= arr.length <= 5 * 10^4`
    - `0 <= arr[i] <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def subarray_bitwise_ors(self, arr: list[int]) -> int:
            raise NotImplementedError('Implement subarray_bitwise_ors')

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
