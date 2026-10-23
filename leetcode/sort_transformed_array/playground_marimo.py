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
    # 360. Sort Transformed Array

    **Medium** · Array, Math, Two Pointers, Sorting

    Given a **sorted** integer array `nums` and three integers `a`, `b` and `c`, apply a quadratic function of the form `f(x) = ax^2 + bx + c` to each element `nums[i]` in the array, and return *the array in a sorted order*.

    ## Examples

    ```
    Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
    Output: [3,9,15,33]
    ```

    ```
    Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
    Output: [-23,-5,1,7]
    ```

    ## Constraints

    - `1 <= nums.length <= 200`
    - `-100 <= nums[i], a, b, c <= 100`
    - `nums` is sorted in **ascending** order.

    **Follow up:** Could you solve it in `O(n)` time?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def sort_transformed_array(self, nums: list[int], a: int, b: int, c: int) -> list[int]:
            raise NotImplementedError('Implement sort_transformed_array')

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
