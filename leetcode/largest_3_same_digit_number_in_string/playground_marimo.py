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
    # 2264. Largest 3-Same-Digit Number in String

    **Easy** · String

    You are given a string `num` representing a large integer. An integer is **good** if it meets the following conditions:

    - It is a **substring** of `num` with length `3`.
    - It consists of only one unique digit.

    Return *the **maximum good** integer as a **string** or an empty string* `"\"` *if no such integer exists*.

    **Note:**

    - A **substring** is a contiguous sequence of characters within a string.
    - There may be **leading zeroes** in `num` or a good integer.

    ## Examples

    ```
    Input: num = "6777133339"
    Output: "777"
    Explanation: There are two distinct good integers: "777" and "333". "777" is the largest, so we return "777".
    ```

    ```
    Input: num = "2300019"
    Output: "000"
    Explanation: "000" is the only good integer.
    ```

    ```
    Input: num = "42352338"
    Output: "\"
    Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
    ```

    ## Constraints

    - 3 <= num.length <= 1000
    - num only consists of digits.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def largest_good_integer(self, num: str) -> str:
            raise NotImplementedError('Implement largest_good_integer')

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
