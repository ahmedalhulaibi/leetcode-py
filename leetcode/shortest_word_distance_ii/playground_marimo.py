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
    # 244. Shortest Word Distance II

    **Medium** · Design, Array, Hash Table, Two Pointers, String

    Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

    Implement the `WordDistance` class:

    - `WordDistance(String[] wordsDict)` initializes the object with the strings array `wordsDict`.
    - `int shortest(String word1, String word2)` returns the shortest distance between `word1` and `word2` in the array `wordsDict`.

    ## Examples

    ```
    Input
    ["WordDistance", "shortest", "shortest"]
    [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
    Output
    [null, 3, 1]

    Explanation
    WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
    wordDistance.shortest("coding", "practice"); // return 3
    wordDistance.shortest("makes", "coding");  // return 1
    ```

    ## Constraints

    - `1 <= wordsDict.length <= 3 * 10^4`
    - `1 <= wordsDict[i].length <= 10`
    - `wordsDict[i]` consists of lowercase English letters.
    - `word1` and `word2` are in `wordsDict`.
    - `word1 != word2`
    - At most `5000` calls will be made to `shortest`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class WordDistance:

        def __init__(self, words_dict: list[str]) -> None:
            raise NotImplementedError('Implement __init__')

        def shortest(self, word1: str, word2: str) -> int:
            raise NotImplementedError('Implement shortest')

    practice_exports = {'WordDistance': WordDistance}
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
