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
    # 2491. Divide Players Into Teams of Equal Skill

    **Medium** · Array, Hash Table, Two Pointers, Sorting

    You are given a positive integer array `skill` of even length `n` where `skill[i]` denotes the skill of the `i<sup>th</sup>` player. Divide the players into `n / 2` teams of size `2` such that the total skill of each team is equal.

    The chemistry of a team is equal to the product of the skills of the players on that team.

    Return the sum of the chemistry of all the teams, or return `-1` if there is no way to divide the players into teams such that the total skill of each team is equal.

    ## Examples

    ```
    Input: skill = [3,2,5,1,3,4]
    Output: 22
    Explanation:
    Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
    The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
    ```

    ```
    Input: skill = [3,4]
    Output: 12
    Explanation:
    The two players form a team with a total skill of 7.
    The chemistry of the team is 3 * 4 = 12.
    ```

    ```
    Input: skill = [1,1,2,3]
    Output: -1
    Explanation:
    There is no way to divide the players into teams such that the total skill of each team is equal.
    ```

    ## Constraints

    - 2 <= skill.length <= 10^5
    - skill.length is even.
    - 1 <= skill[i] <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def divide_players(self, skill: list[int]) -> int:
            raise NotImplementedError('Implement divide_players')

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
