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
    # 1395. Count Number of Teams

    **Medium** · Array, Dynamic Programming, Binary Indexed Tree, Segment Tree

    There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.

    You have to form a team of 3 soldiers amongst them under the following rules:

    - Choose 3 soldiers with index (`i`, `j`, `k`) with rating (`rating[i]`, `rating[j]`, `rating[k]`).
    - A team is valid if: `rating[i] < rating[j] < rating[k]` or `rating[i] > rating[j] > rating[k]` where (`0 <= i < j < k < n`).

    Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

    ## Examples

    ```
    Input: rating = [2,5,3,4,1]
    Output: 3
    Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
    ```

    ```
    Input: rating = [2,1,3]
    Output: 0
    Explanation: We can't form any team given the conditions.
    ```

    ```
    Input: rating = [1,2,3,4]
    Output: 4
    ```

    ## Constraints

    - `n == rating.length`
    - `3 <= n <= 1000`
    - `1 <= rating[i] <= 10^5`
    - All the integers in `rating` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_teams(self, rating: list[int]) -> int:
            raise NotImplementedError('Implement num_teams')

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
