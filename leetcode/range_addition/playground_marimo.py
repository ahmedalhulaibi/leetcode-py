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
    # 370. Range Addition

    **Medium** · Array, Prefix Sum

    You are given an integer `length` and an array `updates` where `updates[i] = [startIdx_i, endIdx_i, inc_i]`.

    You have an array `arr` of length `length` with all zeros, and you have some operation to apply on `arr`. In the `i^th` operation, you should increment all the elements `arr[startIdx_i], arr[startIdx_i + 1], ..., arr[endIdx_i]` by `inc_i`.

    Return `arr` *after applying all the* `updates`.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0370.Range%20Addition/images/rangeadd-grid.jpg)

    ```
    Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
    Output: [-2,0,3,5,3]
    ```

    ```
    Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
    Output: [0,-4,2,2,2,4,4,-4,-4,-4]
    ```

    ## Constraints

    - `1 <= length <= 10^5`
    - `0 <= updates.length <= 10^4`
    - `0 <= startIdx_i <= endIdx_i < length`
    - `-1000 <= inc_i <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_modified_array(self, length: int, updates: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement get_modified_array')

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
