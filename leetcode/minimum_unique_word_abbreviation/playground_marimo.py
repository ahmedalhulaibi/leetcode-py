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
    # 411. Minimum Unique Word Abbreviation

    **Hard** · Bit Manipulation, Array, String, Backtracking

    A string can be **abbreviated** by replacing any number of **non-adjacent** substrings with their lengths. For example, a string such as `"substitution"` could be abbreviated as (but not limited to):

    - `"s10n"` (`"s ubstitutio n"`)
    - `"sub4u4"` (`"sub stit u tion"`)
    - `"12"` (`"substitution"`)
    - `"su3i1u2on"` (`"su bst i t u ti on"`)
    - `"substitution"` (no substrings replaced)

    Note that `"s55n"` (`"s ubsti tutio n"`) is not a valid abbreviation of `"substitution"` because the replaced substrings are adjacent.

    The **length** of an abbreviation is the number of letters that were not replaced plus the number of substrings that were replaced. For example, the abbreviation `"s10n"` has a length of `3` (`2` letters + `1` substring) and `"su3i1u2on"` has a length of `9` (`6` letters + `3` substrings).

    Given a target string `target` and an array of strings `dictionary`, return *an **abbreviation** of* `target`* with the **shortest possible length** such that it is **not an abbreviation** of **any** string in* `dictionary`*. If there are multiple shortest abbreviations, return any of them*.

    ## Examples

    ```
    Input: target = "apple", dictionary = ["blade"]
    Output: "a4"
    Explanation: The shortest abbreviation of "apple" is "5", but this is also an abbreviation of "blade".
    The next shortest abbreviations are "a4" and "4e". "4e" is an abbreviation of blade while "a4" is not.
    Hence, return "a4".
    ```

    ```
    Input: target = "apple", dictionary = ["blade","plain","amber"]
    Output: "1p3"
    Explanation: "5" is an abbreviation of both "apple" but also every word in the dictionary.
    "a4" is an abbreviation of "apple" but also "amber".
    "4e" is an abbreviation of "apple" but also "blade".
    "1p3", "2p2", and "3l1" are the next shortest abbreviations of "apple".
    Since none of them are abbreviations of words in the dictionary, returning any of them is correct.
    ```

    ## Constraints

    - `m == target.length`
    - `n == dictionary.length`
    - `1 <= m <= 21`
    - `0 <= n <= 1000`
    - `1 <= dictionary[i].length <= 100`
    - `log_2(n) + m <= 21` if `n > 0`
    - `target` and `dictionary[i]` consist of lowercase English letters.
    - `dictionary` does not contain `target`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_abbreviation(self, target: str, dictionary: list[str]) -> str:
            raise NotImplementedError('Implement min_abbreviation')

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
