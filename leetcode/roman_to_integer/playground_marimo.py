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
    # 13. Roman to Integer

    **Easy** · Hash Table, Math, String

    Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

    **Symbol**       **Value**
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

    - `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
    - `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
    - `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer.

    ## Examples

    ```
    Input: s = "III"
    Output: 3
    Explanation: III = 3.
    ```

    ```
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    ```

    ```
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    ```

    ## Constraints

    - 1 <= s.length <= 15
    - `s` contains only the characters (`'I'`, `'V'`, `'X'`, `'L'`, `'C'`, `'D'`, `'M'`).
    - It is guaranteed that `s` is a valid roman numeral in the range `[1, 3999]`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def roman_to_int(self, s: str) -> int:
            raise NotImplementedError('Implement roman_to_int')

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
