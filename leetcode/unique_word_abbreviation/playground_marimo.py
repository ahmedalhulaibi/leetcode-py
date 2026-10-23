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
    # 288. Unique Word Abbreviation

    **Medium** · Design, Array, Hash Table, String

    The **abbreviation** of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an **abbreviation** of itself.

    For example:

    - `dog -> d1g` because there is one letter between the first letter `d` and the last letter `g`.
    - `internationalization -> i18n` because there are 18 letters between the first letter `i` and the last letter `n`.
    - `it -> it` because any word with only two characters is an **abbreviation** of itself.

    Implement the `ValidWordAbbr` class:

    - `ValidWordAbbr(String[] dictionary)` Initializes the object with a `dictionary` of words.
    - `boolean isUnique(string word)` Returns `true` if **either** of the following conditions are met (otherwise returns `false`):
      - There is no word in `dictionary` whose **abbreviation** is equal to `word`'s **abbreviation**.
      - For any word in `dictionary` whose **abbreviation** is equal to `word`'s **abbreviation**, that word and `word` are **the same**.

    ## Examples

    ```
    Input
    ["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
    [[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
    Output
    [null, false, true, false, true, true]

    Explanation
    ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
    validWordAbbr.isUnique("dear"); // return false, "deer" and "dear" share "d2r" but differ.
    validWordAbbr.isUnique("cart"); // return true, no dictionary word abbreviates to "c2t".
    validWordAbbr.isUnique("cane"); // return false, "cake" and "cane" share "c2e" but differ.
    validWordAbbr.isUnique("make"); // return true, no dictionary word abbreviates to "m2e".
    validWordAbbr.isUnique("cake"); // return true, "cake" is the only word with "c2e".
    ```

    ## Constraints

    - `1 <= dictionary.length <= 3 * 10^4`
    - `1 <= dictionary[i].length <= 20`
    - `dictionary[i]` consists of lowercase English letters.
    - `1 <= word.length <= 20`
    - `word` consists of lowercase English letters.
    - At most `5000` calls will be made to `isUnique`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class ValidWordAbbr:

        def __init__(self, dictionary: list[str]) -> None:
            raise NotImplementedError('Implement __init__')

        def is_unique(self, word: str) -> bool:
            raise NotImplementedError('Implement is_unique')

    practice_exports = {'ValidWordAbbr': ValidWordAbbr}
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
