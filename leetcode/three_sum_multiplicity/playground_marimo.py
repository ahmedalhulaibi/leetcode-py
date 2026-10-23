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
    # 923. 3Sum With Multiplicity

    **Medium** · Array, Hash Table, Two Pointers, Sorting, Counting

    Given an integer array `arr`, and an integer `target`, return the number of tuples `i, j, k` such that `i < j < k` and `arr[i] + arr[j] + arr[k] == target`.

    As the answer can be very large, return it **modulo** `10^9 + 7`.

    ## Examples

    ```
    Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
    Output: 20
    Explanation:
    Enumerating by the values (arr[i], arr[j], arr[k]):
    (1, 2, 5) occurs 8 times;
    (1, 3, 4) occurs 8 times;
    (2, 2, 4) occurs 2 times;
    (2, 3, 3) occurs 2 times.
    ```

    ```
    Input: arr = [1,1,2,2,2,2], target = 5
    Output: 12
    Explanation:
    arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
    We choose one 1 from [1,1] in 2 ways,
    and two 2s from [2,2,2,2] in 6 ways.
    ```

    ```
    Input: arr = [2,1,3], target = 6
    Output: 1
    Explanation: (1, 2, 3) occured one time in the array so we return 1.
    ```

    ## Constraints

    - `3 <= arr.length <= 3000`
    - `0 <= arr[i] <= 100`
    - `0 <= target <= 300`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def three_sum_multiplicity(self, arr: list[int], target: int) -> int:
            raise NotImplementedError('Implement three_sum_multiplicity')

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
