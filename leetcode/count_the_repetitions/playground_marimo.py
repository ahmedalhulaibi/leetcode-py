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
    # 466. Count The Repetitions

    **Hard** · Two Pointers, String, Dynamic Programming

    We define `str = [s, n]` as the string `str` which consists of the string `s` concatenated `n` times.

    - For example, `str == ["abc", 3] =="abcabcabc"`.

    We define that string `s1` can be obtained from string `s2` if we can remove some characters from `s2` such that it becomes `s1`.

    - For example, `s1 = "abc"` can be obtained from `s2 = "abdbec"` based on our definition by removing the bolded underlined characters.

    You are given two strings `s1` and `s2` and two integers `n1` and `n2`. You have the two strings `str1 = [s1, n1]` and `str2 = [s2, n2]`.

    Return *the maximum integer* `m` *such that* `str = [str2, m]` *can be obtained from* `str1`.

    ## Examples

    ```
    Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
    Output: 2
    ```

    ```
    Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
    Output: 1
    ```

    ## Constraints

    - 1 <= s1.length, s2.length <= 100
    - s1 and s2 consist of lowercase English letters.
    - 1 <= n1, n2 <= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_max_repetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
            raise NotImplementedError('Implement get_max_repetitions')

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
