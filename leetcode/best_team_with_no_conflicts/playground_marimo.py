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
    # 1626. Best Team With No Conflicts

    **Medium** · Array, Dynamic Programming, Sorting

    You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the **sum** of scores of all the players in the team.

    However, the basketball team is not allowed to have **conflicts**. A **conflict** exists if a younger player has a **strictly higher** score than an older player. A conflict does **not** occur between players of the same age.

    Given two lists, `scores` and `ages`, where each `scores[i]` and `ages[i]` represents the score and age of the `i`th player, respectively, return *the highest overall score of all possible basketball teams*.

    ## Examples

    ```
    Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
    Output: 34
    Explanation: You can choose all the players.
    ```

    ```
    Input: scores = [4,5,6,5], ages = [2,1,2,1]
    Output: 16
    Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
    ```

    ```
    Input: scores = [1,2,3,5], ages = [8,9,10,1]
    Output: 6
    Explanation: It is best to choose the first 3 players.
    ```

    ## Constraints

    - 1 <= scores.length, ages.length <= 1000
    - scores.length == ages.length
    - 1 <= scores[i] <= 10^6
    - 1 <= ages[i] <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def best_team_score(self, scores: list[int], ages: list[int]) -> int:
            raise NotImplementedError('Implement best_team_score')

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
