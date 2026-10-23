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
    # 205. Isomorphic Strings

    **Easy** · Hash Table, String

    Given two strings `s` and `t`, determine if they are isomorphic.

    Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

    ## Examples

    ```
    Input: s = "egg", t = "add"
    Output: true
    Explanation: The strings s and t can be made identical by:
    - Mapping 'e' to 'a'.
    - Mapping 'g' to 'd'.
    ```

    ```
    Input: s = "f11", t = "b23"
    Output: false
    Explanation: The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.
    ```

    ```
    Input: s = "paper", t = "title"
    Output: true
    ```

    ## Constraints

    - 1 <= s.length <= 5 * 10^4
    - t.length == s.length
    - s and t consist of any valid ascii character.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_isomorphic(self, s: str, t: str) -> bool:
            raise NotImplementedError('Implement is_isomorphic')

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
