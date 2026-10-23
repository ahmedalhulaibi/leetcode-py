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
    # 472. Concatenated Words

    **Hard** · Array, String, Dynamic Programming, Depth-First Search, Trie

    Given an array of strings `words` (**without duplicates**), return *all the **concatenated words** in the given list of* `words`.

    A **concatenated word** is defined as a string that is comprised entirely of **at least two shorter words (not necessarily distinct)** in the given array.

    ## Examples

    ```
    Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
    "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
    ```

    ```
    Input: words = ["cat","dog","catdog"]
    Output: ["catdog"]
    ```

    ## Constraints

    - `1 <= words.length <= 10^4`
    - `1 <= words[i].length <= 30`
    - `words[i]` consists of only lowercase English letters.
    - All the strings of `words` are unique.
    - `1 <= sum(words[i].length) <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_all_concatenated_words_in_a_dict(self, words: list[str]) -> list[str]:
            raise NotImplementedError('Implement find_all_concatenated_words_in_a_dict')

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
