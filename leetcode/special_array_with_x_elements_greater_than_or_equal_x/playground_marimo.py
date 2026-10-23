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
    # 1608. Special Array With X Elements Greater Than or Equal X

    **Easy** · Array, Binary Search, Sorting

    You are given an array `nums` of non-negative integers. `nums` is considered **special** if there exists a number `x` such that there are **exactly** `x` numbers in `nums` that are **greater than or equal to** `x`.

    Notice that `x` **does not** have to be an element in `nums`.

    Return `x` *if the array is* ***special***, *otherwise, return* `-1`. It can be proven that if `nums` is special, the value for `x` is **unique**.

    ## Examples

    ```
    Input: nums = [3,5]
    Output: 2
    Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
    ```

    ```
    Input: nums = [0,0]
    Output: -1
    Explanation: No numbers fit the criteria for x.
    If x = 0, there should be 0 numbers >= x, but there are 2.
    If x = 1, there should be 1 number >= x, but there are 0.
    If x = 2, there should be 2 numbers >= x, but there are 0.
    x cannot be greater since there are only 2 numbers in nums.
    ```

    ```
    Input: nums = [0,4,3,0,4]
    Output: 3
    Explanation: There are 3 values that are greater than or equal to 3.
    ```

    ## Constraints

    - `1 <= nums.length <= 100`
    - `0 <= nums[i] <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def special_array(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement special_array')

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
