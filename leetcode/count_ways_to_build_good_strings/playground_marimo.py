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
    # 2466. Count Ways To Build Good Strings

    **Medium** · Dynamic Programming

    Given the integers `zero`, `one`, `low`, and `high`, we can construct a string by starting with an empty string, and then at each step perform either of the following:

    - Append the character `'0'` `zero` times.
    - Append the character `'1'` `one` times.

    This can be performed any number of times.

    A **good** string is a string constructed by the above process having a **length** between `low` and `high` (**inclusive**).

    Return *the number of **different** good strings that can be constructed satisfying these properties.* Since the answer can be large, return it **modulo** `10^9 + 7`.

    ## Examples

    ```
    Input: low = 3, high = 3, zero = 1, one = 1
    Output: 8
    Explanation: One possible valid good string is "011".
    It can be constructed as follows: "\" -> "0" -> "01" -> "011".
    All binary strings from "000" to "111" are good strings in this example.
    ```

    ```
    Input: low = 2, high = 3, zero = 1, one = 2
    Output: 5
    Explanation: The good strings are "00", "11", "000", "110", and "011".
    ```

    ## Constraints

    - 1 <= low <= high <= 10^5
    - 1 <= zero, one <= low



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_good_strings(self, low: int, high: int, zero: int, one: int) -> int:
            raise NotImplementedError('Implement count_good_strings')

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
