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
    # 845. Longest Mountain in Array

    **Medium** · Array, Two Pointers, Dynamic Programming, Enumeration

    You may recall that an array `arr` is a **mountain array** if and only if:

    - `arr.length >= 3`
    - There exists some index `i` (**0-indexed**) with `0 < i < arr.length - 1` such that:
      - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
      - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

    Given an integer array `arr`, return *the length of the longest subarray, which is a mountain*. Return `0` if there is no mountain subarray.

    ## Examples

    ```
    Input: arr = [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
    ```

    ```
    Input: arr = [2,2,2]
    Output: 0
    Explanation: There is no mountain.
    ```

    ## Constraints

    - 1 <= arr.length <= 10^4
    - 0 <= arr[i] <= 10^4

    **Follow up:**

    - Can you solve it using only one pass?
    - Can you solve it in `O(1)` space?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def longest_mountain(self, arr: list[int]) -> int:
            raise NotImplementedError('Implement longest_mountain')

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
