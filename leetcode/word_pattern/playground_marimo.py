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
    # 290. Word Pattern

    **Easy** · Hash Table, String

    Given a `pattern` and a string `s`, find if `s` follows the same pattern.

    Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`. Specifically:

    - Each letter in `pattern` maps to **exactly** one unique word in `s`.
    - Each unique word in `s` maps to **exactly** one letter in `pattern`.
    - No two letters map to the same word, and no two words map to the same letter.

    ## Examples

    ```
    Input: pattern = 'abba', s = 'dog cat cat dog'
    Output: true
    Explanation:
    The bijection can be established as:
    - 'a' maps to 'dog'.
    - 'b' maps to 'cat'.
    ```

    ```
    Input: pattern = 'abba', s = 'dog cat cat fish'
    Output: false
    ```

    ```
    Input: pattern = 'aaaa', s = 'dog cat cat dog'
    Output: false
    ```

    ## Constraints

    - 1 <= pattern.length <= 300
    - `pattern` contains only lower-case English letters.
    - 1 <= s.length <= 3000
    - `s` contains only lowercase English letters and spaces `' '`.
    - `s` does not contain any leading or trailing spaces.
    - All the words in `s` are separated by a single space.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def word_pattern(self, pattern: str, s: str) -> bool:
            raise NotImplementedError('Implement word_pattern')

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
