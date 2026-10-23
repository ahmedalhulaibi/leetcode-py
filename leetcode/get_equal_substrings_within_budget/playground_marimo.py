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
    # 1208. Get Equal Substrings Within Budget

    **Medium** · String, Binary Search, Sliding Window, Prefix Sum

    You are given two strings `s` and `t` of the same length and an integer `maxCost`.

    You want to change `s` to `t`. Changing the `i`th character of `s` to `i`th character of `t` costs `|s[i] - t[i]|` (i.e., the absolute difference between the ASCII values of the characters).

    Return *the maximum length of a substring of* `s` *that can be changed to be the same as the corresponding substring of* `t` *with a cost less than or equal to* `maxCost`. If there is no substring from `s` that can be changed to its corresponding substring from `t`, return `0`.

    ## Examples

    ```
    Input: s = "abcd", t = "bcdf", maxCost = 3
    Output: 3
    Explanation: "abc" of s can change to "bcd".
    That costs 3, so the maximum length is 3.
    ```

    ```
    Input: s = "abcd", t = "cdef", maxCost = 3
    Output: 1
    Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
    ```

    ```
    Input: s = "abcd", t = "acde", maxCost = 0
    Output: 1
    Explanation: You cannot make any change, so the maximum length is 1.
    ```

    ## Constraints

    - `1 <= s.length <= 10^5`
    - `t.length == s.length`
    - `0 <= maxCost <= 10^6`
    - `s` and `t` consist of only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def equal_substring(self, s: str, t: str, max_cost: int) -> int:
            raise NotImplementedError('Implement equal_substring')

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
