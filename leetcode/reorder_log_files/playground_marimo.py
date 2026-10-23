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
    # 937. Reorder Data in Log Files

    **Medium** · Array, String, Sorting

    You are given an array of logs. Each log is a space-delimited string of words, where the first word is the **identifier**.

    There are two types of logs:

    - **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
    - **Digit-logs**: All words (except the identifier) consist of digits.

    Reorder these logs so that:

    1. The **letter-logs** come before all **digit-logs**.
    2. The **letter-logs** are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
    3. The **digit-logs** maintain their relative ordering.

    Return *the final order of the logs*.

    ## Examples

    ```
    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    Explanation:
    The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
    The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
    ```

    ```
    Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    ```

    ## Constraints

    - 1 <= logs.length <= 100
    - 3 <= logs[i].length <= 100
    - All the tokens of logs[i] are separated by a single space.
    - logs[i] is guaranteed to have an identifier and at least one word after the identifier.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def reorder_log_files(self, logs: list[str]) -> list[str]:
            raise NotImplementedError('Implement reorder_log_files')

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
