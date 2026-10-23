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
    # 301. Remove Invalid Parentheses

    **Hard** · String, Backtracking, Breadth-First Search

    Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

    Return *a list of **unique strings*** that are valid with the minimum number of removals. You may return the answer in **any order**.

    ## Examples

    ```
    Input: s = "()())()"
    Output: ["(())()","()()()"]
    ```

    ```
    Input: s = "(a)())()"
    Output: ["(a())()","(a)()()"]
    ```

    ```
    Input: s = ")("
    Output: ["\"]
    ```

    ## Constraints

    - `1 <= s.length <= 25`
    - `s` consists of lowercase English letters and parentheses `'('` and `')'`.
    - There will be at most `20` parentheses in `s`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def remove_invalid_parentheses(self, s: str) -> list[str]:
            raise NotImplementedError('Implement remove_invalid_parentheses')

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
