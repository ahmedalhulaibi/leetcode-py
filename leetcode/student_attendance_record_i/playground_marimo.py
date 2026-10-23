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
    # 551. Student Attendance Record I

    **Easy** · String

    You are given a string `s` representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day.

    The record only contains the following three characters:

    - `'A'`: Absent.
    - `'L'`: Late.
    - `'P'`: Present.

    The student is eligible for an attendance award if they meet **both** of the following criteria:

    - The student was absent (`'A'`) for **strictly** fewer than 2 days **total**.
    - The student was **never** late (`'L'`) for 3 or more **consecutive** days.

    Return `true` if the student is eligible for an attendance award, or `false` otherwise.

    ## Examples

    ```
    Input: s = "PPALLP"
    Output: true
    Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
    ```

    ```
    Input: s = "PPALLL"
    Output: false
    Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
    ```

    ## Constraints

    - 1 <= s.length <= 1000
    - s[i] is either 'A', 'L', or 'P'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def check_record(self, s: str) -> bool:
            raise NotImplementedError('Implement check_record')

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
