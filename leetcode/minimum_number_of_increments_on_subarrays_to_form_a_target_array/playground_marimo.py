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
    # 1526. Minimum Number of Increments on Subarrays to Form a Target Array

    **Hard** · Array, Dynamic Programming, Stack, Greedy, Monotonic Stack

    You are given an integer array <code>target</code>. You have an integer array <code>initial</code> of the same size as <code>target</code> with all elements initially zeros.

    In one operation you can choose <strong>any</strong> subarray from <code>initial</code> and increment each value by one.

    Return <em>the minimum number of operations to form a </em><code>target</code><em> array from </em><code>initial</code>.

    The test cases are generated so that the answer fits in a 32-bit integer.

    ## Examples

    ```
    Input: target = [1,2,3,2,1]
    Output: 3
    Explanation: We need at least 3 operations to form the target array from the initial array.
    [0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
    [1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
    [1,2,2,2,1] increment 1 at index 2.
    [1,2,3,2,1] target array is formed.
    ```

    ```
    Input: target = [3,1,1,2]
    Output: 4
    Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
    ```

    ```
    Input: target = [3,1,5,4,2]
    Output: 7
    Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2]
    ```

    ## Constraints

    - 1 <= target.length <= 10^5
    - 1 <= target[i] <= 10^5
    - The input is generated such that the answer fits inside a 32 bit integer.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_number_operations(self, target: list[int]) -> int:
            raise NotImplementedError('Implement min_number_operations')

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
