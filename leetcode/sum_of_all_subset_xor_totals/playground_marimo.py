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
    # 1863. Sum of All Subset XOR Totals

    **Easy** · Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration

    The **XOR total** of an array is defined as the bitwise `XOR` of **all its elements**, or `0` if the array is **empty**.

    - For example, the **XOR total** of the array `[2,5,6]` is `2 XOR 5 XOR 6 = 1`.

    Given an array `nums`, return *the **sum** of all **XOR totals** for every **subset** of* `nums`.

    **Note:** Subsets with the **same** elements should be counted **multiple** times.

    An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`.

    ## Examples

    ```
    Input: nums = [1,3]
    Output: 6
    Explanation: The 4 subsets of [1,3] are:
    - The empty subset has an XOR total of 0.
    - [1] has an XOR total of 1.
    - [3] has an XOR total of 3.
    - [1,3] has an XOR total of 1 XOR 3 = 2.
    0 + 1 + 3 + 2 = 6
    ```

    ```
    Input: nums = [5,1,6]
    Output: 28
    Explanation: The 8 subsets of [5,1,6] are:
    - The empty subset has an XOR total of 0.
    - [5] has an XOR total of 5.
    - [1] has an XOR total of 1.
    - [6] has an XOR total of 6.
    - [5,1] has an XOR total of 5 XOR 1 = 4.
    - [5,6] has an XOR total of 5 XOR 6 = 3.
    - [1,6] has an XOR total of 1 XOR 6 = 7.
    - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
    0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
    ```

    ```
    Input: nums = [3,4,5,6,7,8]
    Output: 480
    Explanation: The sum of all XOR totals for every subset is 480.
    ```

    ## Constraints

    - 1 <= nums.length <= 12
    - 1 <= nums[i] <= 20



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def subset_xor_sum(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement subset_xor_sum')

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
