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
    # 1152. Analyze User Website Visit Pattern

    **Medium** · Array, Hash Table, String, Sorting

    You are given two string arrays `username` and `website` and an integer array `timestamp`. All the given arrays are of the same length and the tuple `[username[i], website[i], timestamp[i]]` indicates that the user `username[i]` visited the website `website[i]` at time `timestamp[i]`.

    A **pattern** is a list of three websites (not necessarily distinct).

    - For example, `['home', 'away', 'love']`, `['leetcode', 'love', 'leetcode']`, and `['luffy', 'luffy', 'luffy']` are all patterns.

    The **score** of a **pattern** is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

    - For example, if the pattern is `['home', 'away', 'love']`, the score is the number of users `x` such that `x` visited `'home'` then visited `'away'` and visited `'love'` after that.
    - Similarly, if the pattern is `['leetcode', 'love', 'leetcode']`, the score is the number of users `x` such that `x` visited `'leetcode'` then visited `'love'` and visited `'leetcode'` one more time after that.
    - Also, if the pattern is `['luffy', 'luffy', 'luffy']`, the score is the number of users `x` such that `x` visited `'luffy'` three different times at different timestamps.

    Return the **pattern** with the largest **score**. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

    Note that the websites in a pattern **do not** need to be visited *contiguously*, they only need to be visited in the order they appeared in the pattern.

    ## Examples

    ```
    Input: username = ['joe','joe','joe','james','james','james','james','mary','mary','mary']
    timestamp = [1,2,3,4,5,6,7,8,9,10]
    website = ['home','about','career','home','cart','maps','home','home','about','career']
    Output: ['home','about','career']
    Explanation: The tuples in this example are:
    ['joe','home',1],['joe','about',2],['joe','career',3],['james','home',4],['james','cart',5],['james','maps',6],['james','home',7],['mary','home',8],['mary','about',9], and ['mary','career',10].
    The pattern ('home', 'about', 'career') has score 2 (joe and mary).
    The pattern ('home', 'cart', 'maps') has score 1 (james).
    The pattern ('home', 'cart', 'home') has score 1 (james).
    The pattern ('home', 'maps', 'home') has score 1 (james).
    The pattern ('cart', 'maps', 'home') has score 1 (james).
    The pattern ('home', 'home', 'home') has score 0 (no user visited home 3 times).
    ```

    ```
    Input: username = ['ua','ua','ua','ub','ub','ub']
    timestamp = [1,2,3,4,5,6]
    website = ['a','b','a','a','b','c']
    Output: ['a','b','a']
    ```

    ## Constraints

    - 3 <= username.length <= 50
    - 1 <= username[i].length <= 10
    - timestamp.length == username.length
    - 1 <= timestamp[i] <= 10^9
    - website.length == username.length
    - 1 <= website[i].length <= 10
    - username[i] and website[i] consist of lowercase English letters.
    - It is guaranteed that there is at least one user who visited at least three websites.
    - All the tuples `[username[i], timestamp[i], website[i]]` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def most_visited_pattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
            raise NotImplementedError('Implement most_visited_pattern')

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
