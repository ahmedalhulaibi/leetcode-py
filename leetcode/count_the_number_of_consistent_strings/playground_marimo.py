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
    # 1684. Count the Number of Consistent Strings

    **Easy** · Array, Hash Table, String, Bit Manipulation, Counting

    You are given a string `allowed` consisting of **distinct** characters and an array of strings `words`. A string is **consistent** if all characters in the string appear in the string `allowed`.

    Return the number of consistent strings in the array `words`.

    ## Examples

    ```
    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
    ```

    ```
    Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
    Output: 7
    Explanation: All strings are consistent.
    ```

    ```
    Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
    Output: 4
    Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
    ```

    ## Constraints

    - 1 <= words.length <= 10^4
    - 1 <= allowed.length <= 26
    - 1 <= words[i].length <= 10
    - The characters in allowed are distinct.
    - words[i] and allowed contain only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_consistent_strings(self, allowed: str, words: list[str]) -> int:
            raise NotImplementedError('Implement count_consistent_strings')

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
