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
    # 443. String Compression

    **Medium** · Two Pointers, String

    Given an array of characters `chars`, compress it using the following algorithm:

    Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:

    - If the group's length is `1`, append the character to `s`.
    - Otherwise, append the character followed by the group's length.

    The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array `chars`**. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

    After you are done **modifying the input array,** return *the new length of the array*.

    You must write an algorithm that uses only constant extra space.

    **Note:** The characters in the array beyond the returned length do not matter and should be ignored.

    ## Examples

    ```
    Input: chars = ["a","a","b","b","c","c","c"]
    Output: 6
    Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
    After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].
    ```

    ```
    Input: chars = ["a"]
    Output: 1
    Explanation: The only group is "a", which remains uncompressed since it is a single character.
    After modifying the input array in-place, the first character of chars should be ["a"].
    ```

    ```
    Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: 4
    Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
    After modifying the input array in-place, the first 4 characters of chars should be ["a","b","1","2"].
    ```

    ## Constraints

    - `1 <= chars.length <= 2000`
    - `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def compress(self, chars: list[str]) -> int:
            raise NotImplementedError('Implement compress')

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
