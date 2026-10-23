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
    # 481. Magical String

    **Medium** · Two Pointers, String

    A magical string `s` consists of only `'1'` and `'2'` and obeys the following rules:

    - Concatenating the sequence of lengths of its consecutive groups of identical characters `'1'` and `'2'` generates the string `s` itself.

    The first few elements of `s` is `s = "1221121221221121122......"`. If we group the consecutive 1's and 2's in `s`, it will be `"1 22 11 2 1 22 1 22 11 2 11 22 ......"` and counting the occurrences of 1's or 2's in each group yields the sequence `"1 2 2 1 1 2 1 2 2 1 2 2 ......"`.

    You can see that concatenating the occurrence sequence gives us `s` itself.

    Given an integer `n`, return the number of 1's in the first n number in the magical string `s`.

    ## Examples

    ```
    Input: n = 6
    Output: 3
    Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
    ```

    ```
    Input: n = 1
    Output: 1
    ```

    ## Constraints

    - 1 <= n <= 10<sup>5</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def magical_string(self, n: int) -> int:
            raise NotImplementedError('Implement magical_string')

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
