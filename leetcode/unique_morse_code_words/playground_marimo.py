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
    # 804. Unique Morse Code Words

    **Easy** · Array, Hash Table, String

    International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

    - `'a'` maps to `".-"`,
    - `'b'` maps to `"-..."`,
    - `'c'` maps to `"-.-."`, and so on.

    For convenience, the full table for the 26 letters of the English alphabet is given below:

    ```
    [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    ```

    Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter.

    - For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and `"-..."`. We will call such a concatenation the **transformation** of a word.

    Return *the number of different transformations among all words we have*.

    ## Examples

    ```
    Input: words = ["gin","zen","gig","msg"]
    Output: 2
    Explanation: The transformation of each word is:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."
    There are 2 different transformations: "--...-." and "--...--.".
    ```

    ```
    Input: words = ["a"]
    Output: 1
    ```

    ## Constraints

    - 1 <= words.length <= 100
    - 1 <= words[i].length <= 12
    - words[i] consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def unique_morse_representations(self, words: list[str]) -> int:
            raise NotImplementedError('Implement unique_morse_representations')

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
