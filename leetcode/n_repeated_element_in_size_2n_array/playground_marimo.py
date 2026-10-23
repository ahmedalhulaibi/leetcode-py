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
    # 961. N-Repeated Element in Size 2N Array

    **Easy** · Array, Hash Table

    You are given an integer array `nums` with the following properties:

    - `nums.length == 2 * n`.
    - `nums` contains `n + 1` **unique** values, `n` of which occur **exactly once** in the array.
    - Exactly one element of `nums` is repeated `n` times.

    Return the element that is repeated `n` times.

    ## Examples

    ```
    Input: nums = [1,2,3,3]
    Output: 3
    ```

    ```
    Input: nums = [2,1,2,5,3,2]
    Output: 2
    ```

    ```
    Input: nums = [5,1,5,2,5,3,5,4]
    Output: 5
    ```

    ## Constraints

    - 2 <= n <= 5000
    - nums.length == 2 * n
    - 0 <= nums[i] <= 10^4
    - nums contains n + 1 unique elements and one of them is repeated exactly n times.

    **Follow-up:** Can you solve it without a hash table, in O(1) extra space?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def repeated_n_times(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement repeated_n_times')

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
