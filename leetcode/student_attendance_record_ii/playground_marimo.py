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
    # 552. Student Attendance Record II

    **Hard** · Dynamic Programming

    An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

    - `'A'`: Absent.
    - `'L'`: Late.
    - `'P'`: Present.

    Any student is eligible for an attendance award if they meet **both** of the following criteria:

    - The student was absent (`'A'`) for **strictly** fewer than 2 days **total**.
    - The student was **never** late (`'L'`) for 3 or more **consecutive** days.

    Given an integer `n`, return *the **number** of possible attendance records of length* `n` *that make a student eligible for an attendance award*. The answer may be very large, so return it **modulo** `10^9 + 7`.

    ## Examples

    ```
    Input: n = 2
    Output: 8
    Explanation: There are 8 records with length 2 that are eligible for an award:
    "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
    Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
    ```

    ```
    Input: n = 1
    Output: 3
    ```

    ```
    Input: n = 10101
    Output: 183236316
    ```

    ## Constraints

    - 1 <= n <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def check_record(self, n: int) -> int:
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
