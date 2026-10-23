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
    # 676. Implement Magic Dictionary

    **Medium** · Hash Table, String, Depth-First Search, Design, Trie

    Design a data structure that is initialized with a list of **different** words. Provided a string, you should determine if you can change **exactly one character** in this string to match any word in the data structure.

    Implement the `MagicDictionary` class:

    - `MagicDictionary()` Initializes the object.
    - `void buildDict(String[] dictionary)` Sets the data structure with an array of distinct strings `dictionary`.
    - `bool search(String searchWord)` Returns `true` if you can change **exactly one character** in `searchWord` to match any string in the data structure, otherwise returns `false`.

    ## Examples

    ```
    Input
    ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
    [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
    Output
    [null, null, false, true, false, false]

    Explanation
    MagicDictionary magicDictionary = new MagicDictionary();
    magicDictionary.buildDict(["hello", "leetcode"]);
    magicDictionary.search("hello"); // return False
    magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
    magicDictionary.search("hell"); // return False
    magicDictionary.search("leetcoded"); // return False
    ```

    ## Constraints

    - `1 <= dictionary.length <= 100`
    - `1 <= dictionary[i].length <= 100`
    - `dictionary[i]` consists of only lower-case English letters.
    - All the strings in `dictionary` are **distinct**.
    - `1 <= searchWord.length <= 100`
    - `searchWord` consists of only lower-case English letters.
    - `buildDict` will be called only once before `search`.
    - At most `100` calls will be made to `search`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MagicDictionary:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def build_dict(self, dictionary: list[str]) -> None:
            raise NotImplementedError('Implement build_dict')

        def search(self, search_word: str) -> bool:
            raise NotImplementedError('Implement search')

    practice_exports = {'MagicDictionary': MagicDictionary}
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
