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
    # 642. Design Search Autocomplete System

    **Hard** · Depth-First Search, Design, Trie, String, Data Stream, Sorting, Heap (Priority Queue)

    Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character `'#'`).

    You are given a string array `sentences` and an integer array `times` both of length `n` where `sentences[i]` is a previously typed sentence and `times[i]` is the corresponding number of times the sentence was typed. For each input character except `'#'`, return the top `3` historical hot sentences that have the same prefix as the part of the sentence already typed.

    Here are the specific rules:

    - The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
    - The returned top `3` hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
    - If less than `3` hot sentences exist, return as many as you can.
    - When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

    Implement the `AutocompleteSystem` class:

    - `AutocompleteSystem(String[] sentences, int[] times)` Initializes the object with the `sentences` and `times` arrays.
    - `List<String> input(char c)` This indicates that the user typed the character `c`.
      - Returns an empty array `[]` if `c == '#'` and stores the inputted sentence in the system.
      - Returns the top `3` historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than `3` matches, return them all.

    ## Examples

    ```
    Input
    ["AutocompleteSystem", "input", "input", "input", "input"]
    [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
    Output
    [null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

    Explanation
    AutocompleteSystem obj = new AutocompleteSystem([...], [5, 3, 2, 2]);
    obj.input("i"); // return ["i love you", "island", "i love leetcode"]
    obj.input(" "); // return ["i love you", "i love leetcode"]
    obj.input("a"); // return []
    obj.input("#"); // return []
    ```

    ## Constraints

    - `n == sentences.length`
    - `n == times.length`
    - `1 <= n <= 100`
    - `1 <= sentences[i].length <= 100`
    - `1 <= times[i] <= 50`
    - `c` is a lowercase English letter, a hash `'#'`, or space `' '`.
    - Each tested sentence will be a sequence of characters `c` that end with the character `'#'`.
    - Each tested sentence will have a length in the range `[1, 200]`.
    - The words in each input sentence are separated by single spaces.
    - At most `5000` calls will be made to `input`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class AutocompleteSystem:

        def __init__(self, sentences: list[str], times: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def input(self, c: str) -> list[str]:
            raise NotImplementedError('Implement input')

    practice_exports = {'AutocompleteSystem': AutocompleteSystem}
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
