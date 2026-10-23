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
    # 824. Goat Latin

    **Easy** · String

    You are given a string `sentence` that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

    We would like to convert the sentence to **Goat Latin** (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

    - If a word begins with a vowel (`'a'`, `'e'`, `'i'`, `'o'`, or `'u'`), append `"ma"` to the end of the word.
      - For example, the word `"apple"` becomes `"applema"`.
    - If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add `"ma"`.
      - For example, the word `"goat"` becomes `"oatgma"`.
    - Add one letter `'a'` to the end of each word per its word index in the sentence, starting with `1`.
      - For example, the first word gets `"a"` added to the end, the second word gets `"aa"` added to the end, and so on.

    Return the final sentence representing the conversion from sentence to Goat Latin.

    ## Examples

    ```
    Input: sentence = "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    ```

    ```
    Input: sentence = "apple"
    Output: "applema"
    ```

    ```
    Input: sentence = "goat"
    Output: "oatgma"
    ```

    ## Constraints

    - 1 <= sentence.length <= 150
    - sentence consists of English letters and spaces.
    - sentence has no leading or trailing spaces.
    - All the words in sentence are separated by a single space.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def to_goat_latin(self, sentence: str) -> str:
            raise NotImplementedError('Implement to_goat_latin')

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
