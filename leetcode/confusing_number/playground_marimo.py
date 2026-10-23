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
    # 1056. Confusing Number

    **Easy** · Math

    A **confusing number** is a number that when rotated `180` degrees becomes a **different** number with each digit valid.

    We can rotate digits of a number by `180` degrees to form new digits.

    - When `0, 1, 6, 8,` and `9` are rotated `180` degrees, they become `0, 1, 9, 8,` and `6` respectively.
    - When `2, 3, 4, 5,` and `7` are rotated `180` degrees, they become **invalid**.

    Note that after rotating a number, we can ignore leading zeros.

    - For example, after rotating `8000`, we have `0008` which is considered as just `8`.

    Given an integer `n`, return `true` *if it is a* **confusing number***, or* `false` *otherwise*.

    ## Examples

    ```
    Input: n = 6
    Output: true
    Explanation: We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
    ```

    ```
    Input: n = 89
    Output: true
    Explanation: We get 68 after rotating 89, 68 is a valid number and 68 != 89.
    ```

    ```
    Input: n = 11
    Output: false
    Explanation: We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.
    ```

    ## Constraints

    - 0 <= n <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def confusing_number(self, n: int) -> bool:
            raise NotImplementedError('Implement confusing_number')

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
