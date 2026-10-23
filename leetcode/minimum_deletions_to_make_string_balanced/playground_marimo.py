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
    # 1653. Minimum Deletions to Make String Balanced

    **Medium** · String, Dynamic Programming, Stack

    You are given a string `s` consisting only of characters `'a'` and `'b'`.

    You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j] = 'a'`.

    Return the minimum number of deletions needed to make `s` balanced.

    ## Examples

    ```
    Input: s = "aababbab"
    Output: 2
    Explanation: You can either:
    Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
    Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
    ```

    ```
    Input: s = "bbaaaaabb"
    Output: 2
    Explanation: The only solution is to delete the first two characters.
    ```

    ## Constraints

    - 1 <= s.length <= 10^5
    - s[i] is 'a' or 'b'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_deletions(self, s: str) -> int:
            raise NotImplementedError('Implement minimum_deletions')

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
