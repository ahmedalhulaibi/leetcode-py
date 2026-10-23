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
    # 1963. Minimum Number of Swaps to Make the String Balanced

    **Medium** · Two Pointers, String, Stack, Greedy, Bracket Sequences

    You are given a **0-indexed** string `s` of **even** length `n`. The string consists of **exactly** `n / 2` opening brackets `'['` and `n / 2` closing brackets `']'`.

    A string is called **balanced** if and only if:

    - It is the empty string, or
    - It can be written as `AB`, where both `A` and `B` are **balanced** strings, or
    - It can be written as `[C]`, where `C` is a **balanced** string.

    You may swap the brackets at **any** two indices **any** number of times.

    Return *the **minimum** number of swaps to make* `s` *balanced*.

    ## Examples

    ```
    Input: s = "][]["
    Output: 1
    Explanation: You can make the string balanced by swapping index 0 with index 3.
    The resulting string is "[[]]".
    ```

    ```
    Input: s = "]]][[["
    Output: 2
    Explanation: You can do the following to make the string balanced:
    - Swap index 0 with index 4. s = "[]][][".
    - Swap index 1 with index 5. s = "[[][]]".
    The resulting string is "[[][]]".
    ```

    ```
    Input: s = "[]"
    Output: 0
    Explanation: The string is already balanced.
    ```

    ## Constraints

    - n == s.length
    - 2 <= n <= 10^6
    - n is even.
    - s[i] is either '[' or ']'.
    - The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_swaps(self, s: str) -> int:
            raise NotImplementedError('Implement min_swaps')

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
