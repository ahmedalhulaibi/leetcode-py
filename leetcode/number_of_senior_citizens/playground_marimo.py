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
    mo.md(r"""
    # 2678. Number of Senior Citizens

    **Easy** · Array, String

    <p>You are given a <strong>0-indexed</strong> array of strings <code>details</code>. Each element of <code>details</code> provides information about a given passenger compressed into a string of length <code>15</code>. The system is such that:</p>

    <ul>
        <li>The first ten characters consist of the phone number of passengers.</li>
        <li>The next character denotes the gender of the person.</li>
        <li>The following two characters are used to indicate the age of the person.</li>
        <li>The last two characters determine the seat allotted to that person.</li>
    </ul>

    <p>Return <em>the number of passengers who are <strong>strictly more than 60 years old</strong></em>.</p>

    ## Examples

    ```
    Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
    Output: 2
    Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.
    ```

    ```
    Input: details = ["1313579440F2036","2921522980M5644"]
    Output: 0
    Explanation: None of the passengers are older than 60.
    ```

    ## Constraints

    - `1 <= details.length <= 100`
    - `details[i].length == 15`
    - `details[i]` consists of digits from `'0'` to `'9'`.
    - `details[i][10]` is either `'M'`, `'F'`, or `'O'`.
    - The phone numbers and seat numbers of the passengers are distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_seniors(self, details: list[str]) -> int:
            raise NotImplementedError('Implement count_seniors')

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
