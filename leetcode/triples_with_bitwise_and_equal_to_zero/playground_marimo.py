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
    # 982. Triples with Bitwise AND Equal To Zero

    **Hard** · Array, Hash Table, Bit Manipulation

    Given an integer array `nums`, return *the number of **AND triples***.

    An **AND triple** is a triple of indices `(i, j, k)` such that:

    - `0 <= i < nums.length`
    - `0 <= j < nums.length`
    - `0 <= k < nums.length`
    - `nums[i] & nums[j] & nums[k] == 0`, where `&` represents the bitwise-AND operator.

    ## Examples

    ```
    Input: nums = [2,1,3]
    Output: 12
    Explanation: We could choose the following i, j, k triples:
    (i=0, j=0, k=1) : 2 & 2 & 1
    (i=0, j=1, k=0) : 2 & 1 & 2
    (i=0, j=1, k=1) : 2 & 1 & 1
    (i=0, j=1, k=2) : 2 & 1 & 3
    (i=0, j=2, k=1) : 2 & 3 & 1
    (i=1, j=0, k=0) : 1 & 2 & 2
    (i=1, j=0, k=1) : 1 & 2 & 1
    (i=1, j=0, k=2) : 1 & 2 & 3
    (i=1, j=1, k=0) : 1 & 1 & 2
    (i=1, j=2, k=0) : 1 & 3 & 2
    (i=2, j=0, k=1) : 3 & 2 & 1
    (i=2, j=1, k=0) : 3 & 1 & 2
    ```

    ```
    Input: nums = [0,0,0]
    Output: 27
    ```

    ## Constraints

    - `1 <= nums.length <= 1000`
    - `0 <= nums[i] < 2^16`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_triplets(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement count_triplets')

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
