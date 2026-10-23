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
    # 1512. Number of Good Pairs

    **Easy** · Array, Hash Table, Math, Counting

    Given an array of integers `nums`, return *the number of **good pairs***.

    A pair `(i, j)` is called *good* if `nums[i] == nums[j]` and `i` < `j`.

    ## Examples

    ```
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    ```
    **Explanation:** There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

    ```
    Input: nums = [1,1,1,1]
    Output: 6
    ```
    **Explanation:** Each pair in the array are *good*.

    ```
    Input: nums = [1,2,3]
    Output: 0
    ```

    ## Constraints

    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_identical_pairs(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement num_identical_pairs')

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
