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
    # 2370. Longest Ideal Subsequence

    **Medium** · Hash Table, String, Dynamic Programming

    You are given a string `s` consisting of lowercase letters and an integer `k`. We call a string `t` **ideal** if the following conditions are satisfied:

    - `t` is a **subsequence** of the string `s`.
    - The absolute difference in the alphabet order of every two **adjacent** letters in `t` is less than or equal to `k`.

    Return *the length of the **longest** ideal string*.

    A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

    **Note** that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of `'a'` and `'z'` is `25`, not `1`.

    ## Examples

    ```
    Input: s = "acfgbd", k = 2
    Output: 4
    ```
    **Explanation:** The longest ideal string is `"acbd"`. The length of this string is `4`, so `4` is returned.
    Note that `"acfgbd"` is not ideal because `'c'` and `'f'` have a difference of `3` in alphabet order.

    ```
    Input: s = "abcd", k = 3
    Output: 4
    ```
    **Explanation:** The longest ideal string is `"abcd"`. The length of this string is `4`, so `4` is returned.

    ## Constraints

    - `1 <= s.length <= 10^5`
    - `0 <= k <= 25`
    - `s` consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def longest_ideal_string(self, s: str, k: int) -> int:
            raise NotImplementedError('Implement longest_ideal_string')

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
