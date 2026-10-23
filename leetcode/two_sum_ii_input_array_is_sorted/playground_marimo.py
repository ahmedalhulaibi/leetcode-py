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
    # 167. Two Sum II - Input Array Is Sorted

    **Medium** · Array, Two Pointers, Binary Search

    Given a **1-indexed** array of integers `numbers` that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

    Return *the indices of the two numbers* `index1` *and* `index2`*, **each incremented by one,** as an integer array* `[index1, index2]` *of length 2.*

    The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

    Your solution must use only constant extra space.

    ## Examples

    ```
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    ```
    **Explanation:** The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2. We return [1, 2].

    ```
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    ```
    **Explanation:** The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

    ```
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    ```
    **Explanation:** The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

    ## Constraints

    - 2 <= numbers.length <= 3 * 10^4
    - -1000 <= numbers[i] <= 1000
    - `numbers` is sorted in **non-decreasing order**.
    - -1000 <= target <= 1000
    - The tests are generated such that there is **exactly one solution**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def two_sum(self, numbers: list[int], target: int) -> list[int]:
            raise NotImplementedError('Implement two_sum')

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
