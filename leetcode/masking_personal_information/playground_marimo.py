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
    # 831. Masking Personal Information

    **Medium** · String

    You are given a personal information string `s`, representing either an **email address** or a **phone number**. Return *the **masked** personal information using the below rules*.

    <u>**Email address:**</u>

    An email address is:

    - A **name** consisting of **at least** two uppercase and lowercase English letters, followed by
    - The `'@'` symbol, followed by
    - The **domain** consisting of uppercase and lowercase English letters with a dot `'.'` somewhere in the middle (not the first or last character).

    To mask an email:

    - The uppercase letters in the **name** and **domain** must be converted to lowercase letters.
    - The middle letters of the **name** (i.e., all but the first and last letters) must be replaced by 5 asterisks `"*****"`.

    <u>**Phone number:**</u>

    A phone number is formatted as follows:

    - The phone number contains 10-13 digits.
    - The last 10 digits make up the **local number**.
    - The remaining 0-3 digits, in the beginning, make up the **country code**.
    - **Separation characters** from the set `{'+', '-', '(', ')', ' '}` separate the above digits in some way.

    To mask a phone number:

    - Remove all **separation characters**.
    - The masked phone number should have the form:
      - `"***-***-XXXX"` if the country code has 0 digits.
      - `"+*-***-***-XXXX"` if the country code has 1 digit.
      - `"+**-***-***-XXXX"` if the country code has 2 digits.
      - `"+***-***-***-XXXX"` if the country code has 3 digits.

    - `"XXXX"` is the last 4 digits of the **local number**.

    ## Examples

    ```
    Input: s = "LeetCode@LeetCode.com"
    Output: "l*****e@leetcode.com"
    Explanation: s is an email address.
    The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
    ```

    ```
    Input: s = "AB@qq.com"
    Output: "a*****b@qq.com"
    Explanation: s is an email address.
    The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
    Note that even though "ab" is 2 characters, it still must have 5 asterisks in the middle.
    ```

    ```
    Input: s = "1(234)567-890"
    Output: "***-***-7890"
    Explanation: s is a phone number.
    There are 10 digits, so the local number is 10 digits and the country code is 0 digits.
    Thus, the resulting masked number is "***-***-7890".
    ```

    ## Constraints

    - s is either a valid email or a phone number.
    - If s is an email:
      - 8 <= s.length <= 40
      - s consists of uppercase and lowercase English letters and exactly one '@' symbol and '.' symbol.
    - If s is a phone number:
      - 10 <= s.length <= 20
      - s consists of digits, spaces, and the symbols '(', ')', '-', and '+'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def mask_pii(self, s: str) -> str:
            raise NotImplementedError('Implement mask_pii')

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
