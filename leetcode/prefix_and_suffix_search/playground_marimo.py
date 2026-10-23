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
    # 745. Prefix and Suffix Search

    **Hard** · Array, Hash Table, String, Design, Trie

    Design a special dictionary that searches the words in it by a prefix and a suffix.

    Implement the `WordFilter` class:

    - `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary.
    - `f(string pref, string suff)` Returns *the index of the word in the dictionary,* which has the prefix `pref` and the suffix `suff`. If there is more than one valid index, return **the largest** of them. If there is no such word in the dictionary, return `-1`.

    ## Examples

    ```
    Input
    ["WordFilter", "f"]
    [[["apple"]], ["a", "e"]]
    Output
    [null, 0]

    Explanation
    WordFilter wordFilter = new WordFilter(["apple"]);
    wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
    ```

    ## Constraints

    - `1 <= words.length <= 10^4`
    - `1 <= words[i].length <= 7`
    - `1 <= pref.length, suff.length <= 7`
    - `words[i]`, `pref` and `suff` consist of lowercase English letters only.
    - At most `10^4` calls will be made to the function `f`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class WordFilter:

        def __init__(self, words: list[str]) -> None:
            raise NotImplementedError('Implement __init__')

        def f(self, pref: str, suff: str) -> int:
            raise NotImplementedError('Implement f')

    practice_exports = {'WordFilter': WordFilter}
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
