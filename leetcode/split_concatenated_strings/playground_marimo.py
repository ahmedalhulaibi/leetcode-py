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
    # 555. Split Concatenated Strings

    **Medium** · Greedy, Array, String

    You are given an array of strings `strs`. You could concatenate these strings together into a loop, where for each string, you could choose to reverse it or not. Among all the possible loops

    Return the lexicographically largest string after cutting the loop, which will make the looped string into a regular one.

    Specifically, to find the lexicographically largest string, you need to experience two phases:

    1. Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.
    2. Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.

    And your job is to find the lexicographically largest one among all the possible regular strings.

    ## Examples

    ```
    Input: strs = ["abc","xyz"]
    Output: "zyxcba"
    Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-", where '-' represents the looped status. The answer string came from the fourth looped one, where you could cut from the middle character 'a' and get "zyxcba".
    ```

    ```
    Input: strs = ["abc"]
    Output: "cba"
    ```

    ## Constraints

    - `1 <= strs.length <= 1000`
    - `1 <= strs[i].length <= 1000`
    - `1 <= sum(strs[i].length) <= 1000`
    - `strs[i]` consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def split_looping_string(self, strs: list[str]) -> str:
            raise NotImplementedError('Implement split_looping_string')

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
