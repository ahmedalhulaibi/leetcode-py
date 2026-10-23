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
    # 2418. Sort the People

    **Easy** · Array, Hash Table, String, Sorting

    You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

    For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `i<sup>th</sup>` person.

    Return `names`* sorted in **descending** order by the people's heights*.

    ## Examples

    ```
    Input: names = ["Mary","John","Emma"], heights = [180,165,170]
    Output: ["Mary","Emma","John"]
    Explanation: Mary is the tallest, followed by Emma and John.
    ```

    ```
    Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
    Output: ["Bob","Alice","Bob"]
    Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
    ```

    ## Constraints

    - `n == names.length == heights.length`
    - `1 <= n <= 10^3`
    - `1 <= names[i].length <= 20`
    - `1 <= heights[i] <= 10^5`
    - `names[i]` consists of lower and upper case English letters.
    - All the values of `heights` are distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def sort_people(self, names: list[str], heights: list[int]) -> list[str]:
            raise NotImplementedError('Implement sort_people')

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
