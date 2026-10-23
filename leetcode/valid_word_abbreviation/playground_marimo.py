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
    # 408. Valid Word Abbreviation

    **Easy** · Two Pointers, String

    A string can be **abbreviated** by replacing any number of **non-adjacent**, **non-empty** substrings with their lengths. The lengths **should not** have leading zeros.

    For example, a string such as `"substitution"` could be abbreviated as (but not limited to):

    - `"s10n"` (`"s ubstitutio n"`)
    - `"sub4u4"` (`"sub stit u tion"`)
    - `"12"` (`"substitution"`)
    - `"su3i1u2on"` (`"su bst i t u ti on"`)
    - `"substitution"` (no substrings replaced)

    The following are **not valid** abbreviations:

    - `"s55n"` (`"s ubsti tutio n"`, the replaced substrings are adjacent)
    - `"s010n"` (has leading zeros)
    - `"s0ubstitution"` (replaces an empty substring)

    Given a string `word` and an abbreviation `abbr`, return *whether the string **matches** the given abbreviation*.

    A **substring** is a contiguous **non-empty** sequence of characters within a string.

    ## Examples

    ```
    Input: word = "internationalization", abbr = "i12iz4n"
    Output: true
    Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
    ```

    ```
    Input: word = "apple", abbr = "a2e"
    Output: false
    Explanation: The word "apple" cannot be abbreviated as "a2e".
    ```

    ## Constraints

    - `1 <= word.length <= 20`
    - `1 <= abbr.length <= 20`
    - `word` consists of only lowercase English letters.
    - `abbr` consists of lowercase English letters and digits.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
            raise NotImplementedError('Implement valid_word_abbreviation')

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
