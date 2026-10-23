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
    # 1189. Maximum Number of Balloons

    **Easy** · Hash Table, String, Counting

    Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

    You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG)

    ```
    Input: text = "nlaebolko"
    Output: 1
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG)

    ```
    Input: text = "loonbalxballpoon"
    Output: 2
    ```

    ```
    Input: text = "leetcode"
    Output: 0
    ```

    ## Constraints

    - `1 <= text.length <= 10^4`
    - `text` consists of lower case English letters only.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_number_of_balloons(self, text: str) -> int:
            raise NotImplementedError('Implement max_number_of_balloons')

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
