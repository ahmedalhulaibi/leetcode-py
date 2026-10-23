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
    # 2108. Find First Palindromic String in the Array

    **Easy** · Array, Two Pointers, String

    Given an array of strings `words`, return the first **palindromic** string in the array. If there is no such string, return an **empty string** `"\"`.

    A string is **palindromic** if it reads the same forward and backward.

    ## Examples

    ```
    Input: words = ["abc","car","ada","racecar","cool"]
    Output: "ada"
    ```
    **Explanation:** The first string that is palindromic is "ada". Note that "racecar" is also palindromic, but it is not the first.

    ```
    Input: words = ["notapalindrome","racecar"]
    Output: "racecar"
    ```
    **Explanation:** The first and only string that is palindromic is "racecar".

    ```
    Input: words = ["def","ghi"]
    Output: "\"
    ```
    **Explanation:** There are no palindromic strings, so the empty string is returned.

    ## Constraints

    - `1 <= words.length <= 100`
    - `1 <= words[i].length <= 100`
    - `words[i]` consists only of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def first_palindrome(self, words: list[str]) -> str:
            raise NotImplementedError('Implement first_palindrome')

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
