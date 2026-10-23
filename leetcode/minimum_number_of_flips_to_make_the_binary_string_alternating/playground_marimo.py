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
    # 1888. Minimum Number of Flips to Make the Binary String Alternating

    **Medium** · String, Dynamic Programming, Sliding Window

    You are given a binary string `s`. You are allowed to perform two types of operations on the string in any sequence:

    - **Type-1: Remove** the character at the start of the string `s` and **append** it to the end of the string.
    - **Type-2: Pick** any character in `s` and **flip** its value, i.e., if its value is `'0'` it becomes `'1'` and vice-versa.

    Return *the **minimum** number of **type-2** operations you need to perform* *such that* `s` *becomes **alternating**.*

    The string is called **alternating** if no two adjacent characters are equal.

    - For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.

    ## Examples

    ```
    Input: s = "111000"
    Output: 2
    Explanation: Use the first operation two times to make s = "100011".
    Then, use the second operation on the third and sixth elements to make s = "101010".
    ```

    ```
    Input: s = "010"
    Output: 0
    Explanation: The string is already alternating.
    ```

    ```
    Input: s = "1110"
    Output: 1
    Explanation: Use the second operation on the second element to make s = "1010".
    ```

    ## Constraints

    - `1 <= s.length <= 10^5`
    - `s[i]` is either `'0'` or `'1'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_flips(self, s: str) -> int:
            raise NotImplementedError('Implement min_flips')

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
