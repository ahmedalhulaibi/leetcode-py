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
    # 781. Rabbits in Forest

    **Medium** · Array, Hash Table, Math, Greedy

    There is a forest with an unknown number of rabbits. We asked n rabbits **"How many other rabbits have the same color as you?"** and collected the answers in an integer array `answers` where `answers[i]` is the answer of the `i<sup>th</sup>` rabbit.

    Given the array `answers`, return *the minimum number of rabbits that could be in the forest*.

    ## Examples

    ```
    Input: answers = [1,1,2]
    Output: 5
    Explanation:
    The two rabbits that answered "1" could both be the same color, say red.
    The rabbit that answered "2" can't be red or the answers would be inconsistent.
    Say the rabbit that answered "2" was blue.
    Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
    The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
    ```

    ```
    Input: answers = [10,10,10]
    Output: 11
    ```

    ## Constraints

    - `1 <= answers.length <= 1000`
    - `0 <= answers[i] < 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_rabbits(self, answers: list[int]) -> int:
            raise NotImplementedError('Implement num_rabbits')

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
