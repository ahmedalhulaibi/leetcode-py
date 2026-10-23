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
    # 2516. Take K of Each Character From Left and Right

    **Medium** · Hash Table, String, Sliding Window

    You are given a string `s` consisting of the characters `'a'`, `'b'`, and `'c'` and a non-negative integer `k`. Each minute, you may take either the **leftmost** character of `s`, or the **rightmost** character of `s`.

    Return the **minimum** number of minutes needed for you to take **at least** `k` of each character, or return `-1` if it is not possible to take `k` of each character.

    ## Examples

    ```
    Input: s = "aabaaaacaabc", k = 2
    Output: 8
    Explanation:
    Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
    Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
    A total of 3 + 5 = 8 minutes is needed.
    It can be proven that 8 is the minimum number of minutes needed.
    ```

    ```
    Input: s = "a", k = 1
    Output: -1
    Explanation: It is not possible to take one 'b' or 'c' so return -1.
    ```

    ## Constraints

    - `1 <= s.length <= 10^5`
    - `s` consists of only the letters `'a'`, `'b'`, and `'c'`.
    - `0 <= k <= s.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def take_characters(self, s: str, k: int) -> int:
            raise NotImplementedError('Implement take_characters')

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
