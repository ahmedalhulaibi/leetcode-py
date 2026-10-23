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
    # 354. Russian Doll Envelopes

    **Hard** · Array, Binary Search, Dynamic Programming, Sorting, Longest Increasing Subsequence

    You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi, hi]` represents the width and the height of an envelope.

    One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

    Return *the maximum number of envelopes you can Russian doll (i.e., put one inside the other)*.

    **Note:** You cannot rotate an envelope.

    ## Examples

    ```
    Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    Output: 3
    Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
    ```

    ```
    Input: envelopes = [[1,1],[1,1],[1,1]]
    Output: 1
    ```

    ## Constraints

    - 1 <= envelopes.length <= 10<sup>5</sup>
    - `envelopes[i].length == 2`
    - 1 <= w<sub>i</sub>, h<sub>i</sub> <= 10<sup>5</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from bisect import bisect_left

    class Solution:

        def max_envelopes(self, envelopes: list[list[int]]) -> int:
            raise NotImplementedError('Implement max_envelopes')

    practice_exports = {'bisect_left': bisect_left, 'Solution': Solution}
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
