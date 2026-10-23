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
    # 1400. Construct K Palindrome Strings

    **Medium** · Hash Table, String, Greedy, Counting

    Given a string `s` and an integer `k`, return `true` if you can use all the characters in `s` to construct **non-empty** `k` palindrome strings or `false` otherwise.

    ## Examples

    ```
    Input: s = "annabelle", k = 2
    Output: true
    ```
    **Explanation:** You can construct two palindromes using all characters in `s`. Some possible constructions `"anna" + "elble"`, `"anbna" + "elle"`, `"anellena" + "b"`.

    ```
    Input: s = "leetcode", k = 3
    Output: false
    ```
    **Explanation:** It is impossible to construct 3 palindromes using all the characters of `s`.

    ```
    Input: s = "true", k = 4
    Output: true
    ```
    **Explanation:** The only possible solution is to put each character in a separate string.

    ## Constraints

    - `1 <= s.length <= 10^5`
    - `s` consists of lowercase English letters.
    - `1 <= k <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_construct(self, s: str, k: int) -> bool:
            raise NotImplementedError('Implement can_construct')

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
