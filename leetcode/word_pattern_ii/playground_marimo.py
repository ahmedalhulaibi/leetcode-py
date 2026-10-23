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
    # 291. Word Pattern II

    **Medium** · Hash Table, String, Backtracking

    Given a `pattern` and a string `s`, return `true` *if* `s` *matches the* `pattern`.

    A string `s` **matches** a `pattern` if there is some **bijective mapping** of single characters to **non-empty** strings such that if each character in `pattern` is replaced by the string it maps to, then the resulting string is `s`. A **bijective mapping** means that no two characters map to the same string, and no character maps to two different strings.

    ## Examples

    ```
    Input: pattern = "abab", s = "redblueredblue"
    Output: true
    Explanation: One possible mapping is as follows:
    'a' -> "red"
    'b' -> "blue"
    ```

    ```
    Input: pattern = "aaaa", s = "asdasdasdasd"
    Output: true
    Explanation: One possible mapping is as follows:
    'a' -> "asd"
    ```

    ```
    Input: pattern = "aabb", s = "xyzabcxzyabc"
    Output: false
    ```

    ## Constraints

    - `1 <= pattern.length, s.length <= 20`
    - `pattern` and `s` consist of only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def word_pattern_match(self, pattern: str, s: str) -> bool:
            raise NotImplementedError('Implement word_pattern_match')

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
