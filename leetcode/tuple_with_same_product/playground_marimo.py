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
    # 1726. Tuple with Same Product

    **Medium** · Array, Hash Table, Counting

    Given an array `nums` of **distinct** positive integers, return *the number of tuples* `(a, b, c, d)` *such that* `a * b = c * d` *where* `a`, `b`, `c`, and `d` *are elements of* `nums`*, and* `a != b != c != d`.

    ## Examples

    ```
    Input: nums = [2,3,4,6]
    Output: 8
    Explanation: There are 8 valid tuples:
    (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
    (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
    ```

    ```
    Input: nums = [1,2,4,5,10]
    Output: 16
    Explanation: There are 16 valid tuples:
    (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
    (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
    (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
    (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
    ```

    ## Constraints

    - 1 <= nums.length <= 1000
    - 1 <= nums[i] <= 10^4
    - All elements in nums are distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def tuple_same_product(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement tuple_same_product')

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
