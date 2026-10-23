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
    # 820. Short Encoding of Words

    **Medium** · Array, Hash Table, String, Trie

    A **valid encoding** of an array of `words` is any reference string `s` and array of indices `indices` such that:

    - `words.length == indices.length`
    - The reference string `s` ends with the `'#'` character.
    - For each index `indices[i]`, the **substring** of `s` starting from `indices[i]` and up to (but not including) the next `'#'` character is equal to `words[i]`.

    Given an array of `words`, return *the **length of the shortest reference string** * `s` * possible of any **valid encoding** of * `words`*.

    ## Examples

    ```
    Input: words = ["time", "me", "bell"]
    Output: 10
    Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
    words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
    words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "ti*me*#bell#"
    words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#*bell*#"
    ```

    ```
    Input: words = ["t"]
    Output: 2
    Explanation: A valid encoding would be s = "t#" and indices = [0].
    ```

    ## Constraints

    - 1 <= words.length <= 2000
    - 1 <= words[i].length <= 7
    - words[i] consists of only lowercase letters.

    **Follow up:** Can you solve it in O(n * max(words[i].length)) time using a Trie?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_length_encoding(self, words: list[str]) -> int:
            raise NotImplementedError('Implement minimum_length_encoding')

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
