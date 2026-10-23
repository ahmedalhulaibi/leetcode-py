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
    # 1100. Find K-Length Substrings With No Repeated Characters

    **Medium** · Hash Table, String, Sliding Window

    Given a string `s` and an integer `k`, return *the number of substrings in* `s` *of length* `k` *with no repeated characters*.

    ## Examples

    ```
    Input: s = "havefunonleetcode", k = 5
    Output: 6
    Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
    ```

    ```
    Input: s = "home", k = 5
    Output: 0
    Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
    ```

    ## Constraints

    - 1 <= s.length <= 10^4
    - s consists of lowercase English letters.
    - 1 <= k <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_k_len_substr_no_repeats(self, s: str, k: int) -> int:
            raise NotImplementedError('Implement num_k_len_substr_no_repeats')

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
