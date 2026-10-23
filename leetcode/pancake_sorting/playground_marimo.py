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
    # 969. Pancake Sorting

    **Medium** · Array, Two Pointers, Greedy, Sorting

    Given an array of integers `arr`, sort the array by performing a series of **pancake flips**.

    In one pancake flip we do the following steps:

    - Choose an integer `k` where `1 <= k <= arr.length`.
    - Reverse the sub-array `arr[0...k-1]` (0-indexed).

    For example, if `arr = [3,2,1,4]` and we performed a pancake flip choosing `k = 3`, we reverse the sub-array `[3,2,1]`, so `arr = [1,2,3,4]` after the pancake flip at `k = 3`.

    Return an array of the `k`-values corresponding to a sequence of pancake flips that sort `arr`. Any valid answer that sorts the array within `10 * arr.length` flips will be judged as correct.

    ## Examples

    ```
    Input: arr = [3,2,4,1]
    Output: [4,2,4,3]
    Explanation:
    We perform 4 pancake flips, with k values 4, 2, 4, and 3.
    Starting state: arr = [3, 2, 4, 1]
    After 1st flip (k = 4): arr = [1, 4, 2, 3]
    After 2nd flip (k = 2): arr = [4, 1, 2, 3]
    After 3rd flip (k = 4): arr = [3, 2, 1, 4]
    After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
    ```

    ```
    Input: arr = [1,2,3]
    Output: []
    Explanation: The input is already sorted, so there is no need to flip anything.
    Note that other answers, such as [3, 3], would also be accepted.
    ```

    ## Constraints

    - `1 <= arr.length <= 100`
    - `1 <= arr[i] <= arr.length`
    - All integers in `arr` are **unique** (i.e. `arr` is a permutation of the integers from `1` to `arr.length`).



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def pancake_sort(self, arr: list[int]) -> list[int]:
            raise NotImplementedError('Implement pancake_sort')

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
