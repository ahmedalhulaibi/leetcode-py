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
    # 422. Valid Word Square

    **Easy** · Array, Matrix

    Given an array of strings `words`, return `true` *if it forms a valid **word square***.

    A sequence of strings forms a valid **word square** if the `k^th` row and column read the same string, where `0 <= k < max(numRows, numColumns)`.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0422.Valid%20Word%20Square/images/validsq1-grid.jpg)

    ```
    Input: words = ["abcd","bnrt","crmy","dtye"]
    Output: true
    Explanation:
    The 1st row and 1st column both read "abcd".
    The 2nd row and 2nd column both read "bnrt".
    The 3rd row and 3rd column both read "crmy".
    The 4th row and 4th column both read "dtye".
    Therefore, it is a valid word square.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0422.Valid%20Word%20Square/images/validsq2-grid.jpg)

    ```
    Input: words = ["abcd","bnrt","crm","dt"]
    Output: true
    Explanation:
    The 1st row and 1st column both read "abcd".
    The 2nd row and 2nd column both read "bnrt".
    The 3rd row and 3rd column both read "crm".
    The 4th row and 4th column both read "dt".
    Therefore, it is a valid word square.
    ```

    ![Example 3](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0422.Valid%20Word%20Square/images/validsq3-grid.jpg)

    ```
    Input: words = ["ball","area","read","lady"]
    Output: false
    Explanation:
    The 3rd row reads "read" while the 3rd column reads "lead".
    Therefore, it is NOT a valid word square.
    ```

    ## Constraints

    - `1 <= words.length <= 500`
    - `1 <= words[i].length <= 500`
    - `words[i]` consists of only lower-case English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def valid_word_square(self, words: list[str]) -> bool:
            raise NotImplementedError('Implement valid_word_square')

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
