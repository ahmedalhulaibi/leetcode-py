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
    # 2145. Count the Hidden Sequences

    **Medium** · Array, Prefix Sum

    You are given a 0-indexed array `differences` of `n` integers, which describes the differences between each pair of consecutive integers of a hidden sequence of length `n + 1`. You are also given two integers `lower` and `upper` that describe the inclusive range of values that the hidden sequence can contain. Return the number of possible hidden sequences. If there are no possible sequences, return 0.

    ## Examples

    ```text
    Input: differences = [1,-3,4], lower = 1, upper = 6
    Output: 2
    Explanation: The possible hidden sequences are:
    - [3, 4, 1, 5]
    - [4, 5, 2, 6]
    ```

    ```text
    Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
    Output: 4
    ```

    ```text
    Input: differences = [4,-7,2], lower = 3, upper = 6
    Output: 0
    ```

    ## Constraints

    - `n == differences.length`
    - `1 <= n <= 10^5`
    - `-10^5 <= differences[i] <= 10^5`
    - `-10^5 <= lower <= upper <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def number_of_arrays(self, differences: list[int], lower: int, upper: int) -> int:
            raise NotImplementedError('Implement number_of_arrays')

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
