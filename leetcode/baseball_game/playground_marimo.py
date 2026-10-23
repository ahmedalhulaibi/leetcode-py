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
    # 682. Baseball Game

    **Easy** · Array, Stack, Simulation

    You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

    You are given a list of strings `operations`, where `operations[i]` is the `ith` operation you must apply to the record and is one of the following:

    - An integer `x`.
      - Record a new score of `x`.
    - `'+'`.
      - Record a new score that is the sum of the previous two scores.
    - `'D'`.
      - Record a new score that is the double of the previous score.
    - `'C'`.
      - Invalidate the previous score, removing it from the record.

    Return the sum of all the scores on the record after applying all the operations.

    The test cases are generated such that the answer and all intermediate calculations fit in a **32-bit** integer and that all operations are valid.

    ## Examples

    ```
    Input: ops = ["5","2","C","D","+"]
    Output: 30
    Explanation:
    "5" - Add 5 to the record, record is now [5].
    "2" - Add 2 to the record, record is now [5, 2].
    "C" - Invalidate and remove the previous score, record is now [5].
    "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
    "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
    The total sum is 5 + 10 + 15 = 30.
    ```

    ```
    Input: ops = ["5","-2","4","C","D","9","+","+"]
    Output: 27
    ```

    ```
    Input: ops = ["1","C"]
    Output: 0
    ```

    ## Constraints

    - 1 <= operations.length <= 1000
    - `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
    - For operation `"+"`, there will always be at least two previous scores on the record.
    - For operations `"C"` and `"D"`, there will always be at least one previous score on the record.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def cal_points(self, operations: list[str]) -> int:
            raise NotImplementedError('Implement cal_points')

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
