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
    # 1813. Sentence Similarity III

    **Medium** · Array, Two Pointers, String

    You are given two strings `sentence1` and `sentence2`, each representing a **sentence** composed of words. A sentence is a list of **words** that are separated by a **single** space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

    Two sentences `s1` and `s2` are considered **similar** if it is possible to insert an arbitrary sentence (*possibly empty*) inside one of these sentences such that the two sentences become equal. **Note** that the inserted sentence must be separated from existing words by spaces.

    For example,

    - `s1 = "Hello Jane"` and `s2 = "Hello my name is Jane"` can be made equal by inserting `"my name is"` between `"Hello"` and `"Jane"` in `s1`.
    - `s1 = "Frog cool"` and `s2 = "Frogs are cool"` are **not** similar, since although there is a sentence `"s are"` inserted into `s1`, it is not separated from `"Frog"` by a space.

    Given two sentences `sentence1` and `sentence2`, return `true` if `sentence1` and `sentence2` are similar. Otherwise, return `false`.

    ## Examples

    ```
    Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
    Output: true
    ```

    sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

    ```
    Input: sentence1 = "of", sentence2 = "A lot of words"
    Output: false
    ```

    No single sentence can be inserted inside one of the sentences to make it equal to the other.

    ```
    Input: sentence1 = "Eating right now", sentence2 = "Eating"
    Output: true
    ```

    sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

    ## Constraints

    - 1 <= sentence1.length, sentence2.length <= 100
    - sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
    - The words in sentence1 and sentence2 are separated by a single space.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def are_sentences_similar(self, sentence1: str, sentence2: str) -> bool:
            raise NotImplementedError('Implement are_sentences_similar')

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
