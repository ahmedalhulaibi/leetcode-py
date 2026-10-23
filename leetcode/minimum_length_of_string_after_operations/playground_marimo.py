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
    # 3223. Minimum Length of String After Operations

    **Medium** · Hash Table, String, Counting

    You are given a string `s`.

    You can perform the following process on `s` any number of times:

    - Choose an index `i` in the string such that there is **at least** one character to the left of index `i` that is equal to `s[i]`, and **at least** one character to the right that is also equal to `s[i]`.
    - Delete the **closest** occurrence of `s[i]` located to the **left** of `i`.
    - Delete the **closest** occurrence of `s[i]` located to the **right** of `i`.

    Return the **minimum** length of the final string `s` that you can achieve.

    ## Examples

    ```
    Input: s = "abaacbcbb"
    Output: 5
    Explanation:
    We do the following operations:

    - Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
    - Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".
    ```

    ```
    Input: s = "aa"
    Output: 2
    Explanation:
    We cannot perform any operations, so we return the length of the original string.
    ```

    ## Constraints

    - 1 <= s.length <= 2 * 10^5
    - s consists only of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_length(self, s: str) -> int:
            raise NotImplementedError('Implement minimum_length')

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
