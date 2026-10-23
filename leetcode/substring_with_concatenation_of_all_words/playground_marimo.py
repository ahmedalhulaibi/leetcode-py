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
    # 30. Substring with Concatenation of All Words

    **Hard** · Hash Table, String, Sliding Window

    You are given a string `s` and an array of strings `words`. All the strings of `words` are of **the same length**.

    A **concatenated string** is a string that exactly contains all the strings of any permutation of `words` concatenated.

    - For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of `words`.

    ## Examples

    ```
    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]
    ```
    **Explanation:**
    The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of `words`.
    The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of `words`.

    ```
    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    Output: []
    ```
    **Explanation:**
    There is no concatenated substring.

    ```
    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]
    ```
    **Explanation:**
    The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
    The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
    The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

    ## Constraints

    - 1 <= s.length <= 10^4
    - 1 <= words.length <= 5000
    - 1 <= words[i].length <= 30
    - s and words[i] consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_substring(self, s: str, words: list[str]) -> list[int]:
            raise NotImplementedError('Implement find_substring')

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
