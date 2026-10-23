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
    # 1846. Maximum Element After Decreasing and Rearranging

    **Medium** · Array, Greedy, Sorting

    You are given an array of positive integers `arr`. Perform some operations (possibly none) on `arr` so that it satisfies these conditions:

    - The value of the first element in `arr` must be 1.
    - The absolute difference between any 2 adjacent elements must be less than or equal to 1. In other words, `abs(arr[i] - arr[i - 1]) <= 1` for each `i` where `1 <= i < arr.length` (0-indexed). `abs(x)` is the absolute value of `x`.

    There are 2 types of operations that you can perform any number of times:

    - Decrease the value of any element of `arr` to a smaller positive integer.
    - Rearrange the elements of `arr` to be in any order.

    Return *the **maximum** possible value of an element in* `arr` *after performing the operations to satisfy the conditions*.

    ## Examples

    ```
    Input: arr = [2,2,1,2,1]
    Output: 2
    ```
    **Explanation:** We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1]. The largest element in arr is 2.

    ```
    Input: arr = [100,1,1000]
    Output: 3
    ```
    **Explanation:** Rearrange arr so it becomes [1,100,1000]. Decrease the second element to 2 and the third element to 3. Now arr = [1,2,3], which satisfies the conditions. The largest element in arr is 3.

    ```
    Input: arr = [1,2,3,4,5]
    Output: 5
    ```
    **Explanation:** The array already satisfies the conditions, and the largest element is 5.

    ## Constraints

    - 1 <= arr.length <= 10^5
    - 1 <= arr[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_element(self, arr: list[int]) -> int:
            raise NotImplementedError('Implement maximum_element')

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
