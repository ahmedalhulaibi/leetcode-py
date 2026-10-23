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
    # 2140. Solving Questions With Brainpower

    **Medium** · Array, Dynamic Programming

    You are given a **0-indexed** 2D integer array `questions` where `questions[i] = [points<sub>i</sub>, brainpower<sub>i</sub>]`.

    The array describes the questions of an exam, where you have to process the questions **in order** (i.e., starting from question `0`) and make a decision whether to **solve** or **skip** each question. Solving question `i` will **earn** you `points<sub>i</sub>` points but you will be **unable** to solve each of the next `brainpower<sub>i</sub>` questions. If you skip question `i`, you get to make the decision on the next question.

    - For example, given `questions = [[3, 2], [4, 3], [4, 4], [2, 5]]`:
        - If question `0` is solved, you will earn `3` points but you will be unable to solve questions `1` and `2`.
        - If instead, question `0` is skipped and question `1` is solved, you will earn `4` points but you will be unable to solve questions `2` and `3`.

    Return *the **maximum** points you can earn for the exam*.

    ## Examples

    ```
    Input: questions = [[3,2],[4,3],[4,4],[2,5]]
    Output: 5
    Explanation: The maximum points can be earned by solving questions 0 and 3.
    - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
    - Unable to solve questions 1 and 2
    - Solve question 3: Earn 2 points
    Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
    ```

    ```
    Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    Output: 7
    Explanation: The maximum points can be earned by solving questions 1 and 4.
    - Skip question 0
    - Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
    - Unable to solve questions 2 and 3
    - Solve question 4: Earn 5 points
    Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
    ```

    ## Constraints

    - `1 <= questions.length <= 10^5`
    - `questions[i].length == 2`
    - `1 <= points<sub>i</sub>, brainpower<sub>i</sub> <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def most_points(self, questions: list[list[int]]) -> int:
            raise NotImplementedError('Implement most_points')

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
