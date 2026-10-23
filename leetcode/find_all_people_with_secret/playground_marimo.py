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
    # 2092. Find All People With Secret

    **Hard** · Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Sorting

    You are given an integer `n` indicating there are `n` people numbered from `0` to `n - 1`. You are also given a **0-indexed** 2D integer array `meetings` where `meetings[i] = [xi, yi, timei]` indicates that person `xi` and person `yi` have a meeting at `timei`. A person may attend **multiple meetings** at the same time. Finally, you are given an integer `firstPerson`.

    Person `0` has a **secret** and initially shares the secret with a person `firstPerson` at time `0`. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person `xi` has the secret at `timei`, then they will share the secret with person `yi`, and vice versa.

    The secrets are shared **instantaneously**. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

    Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in **any order**.

    ## Examples

    ```
    Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
    Output: [0,1,2,3,5]
    Explanation:
    At time 0, person 0 shares the secret with person 1.
    At time 5, person 1 shares the secret with person 2.
    At time 8, person 2 shares the secret with person 3.
    At time 10, person 1 shares the secret with person 5.
    Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.
    ```

    ```
    Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
    Output: [0,1,3]
    Explanation:
    At time 0, person 0 shares the secret with person 3.
    At time 2, neither person 1 nor person 2 know the secret.
    At time 3, person 3 shares the secret with person 0 and person 1.
    Thus, people 0, 1, and 3 know the secret after all the meetings.
    ```

    ```
    Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
    Output: [0,1,2,3,4]
    Explanation:
    At time 0, person 0 shares the secret with person 1.
    At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
    Note that person 2 can share the secret at the same time as receiving it.
    At time 2, person 3 shares the secret with person 4.
    Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.
    ```

    ## Constraints

    - `2 <= n <= 10^5`
    - `1 <= meetings.length <= 10^5`
    - `meetings[i].length == 3`
    - `0 <= xi, yi <= n - 1`
    - `xi != yi`
    - `1 <= timei <= 10^5`
    - `1 <= firstPerson <= n - 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_all_people(self, n: int, meetings: list[list[int]], first_person: int) -> list[int]:
            raise NotImplementedError('Implement find_all_people')

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
