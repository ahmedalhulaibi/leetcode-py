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
    # 1258. Synonymous Sentences

    **Medium** · Sort, Union Find, Array, Hash Table, String, Backtracking

    You are given a list of equivalent string pairs `synonyms` where `synonyms[i] = [s<sub>i</sub>, t<sub>i</sub>]` indicates that `s<sub>i</sub>` and `t<sub>i</sub>` are equivalent strings. You are also given a sentence `text`.

    Return all possible synonymous sentences **sorted lexicographically**.

    ## Examples

    ```
    Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
    Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
    Explanation: From the synonyms, happy, joy and cheerful are equivalent, and sad and sorrow are equivalent. Replacing each synonymous word independently gives 2 * 3 = 6 sentences.
    ```

    ```
    Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
    Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
    ```

    ## Constraints

    - `0 <= synonyms.length <= 10`
    - `synonyms[i].length == 2`
    - `1 <= s<sub>i</sub>.length, t<sub>i</sub>.length <= 10`
    - `s<sub>i</sub> != t<sub>i</sub>`
    - `text` consists of at most `10` words.
    - All the pairs of `synonyms` are **unique**.
    - The words of `text` are separated by single spaces.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def generate_sentences(self, synonyms: list[list[str]], text: str) -> list[str]:
            raise NotImplementedError('Implement generate_sentences')

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
