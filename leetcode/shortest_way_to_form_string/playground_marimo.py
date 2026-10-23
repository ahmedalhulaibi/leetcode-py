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
    # 1055. Shortest Way to Form String

    **Medium** · String, Dynamic Programming, Greedy

    A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

    Given two strings `source` and `target`, return *the minimum number of subsequences of* `source` *such that their concatenation equals* `target`. If the task is impossible, return `-1`.

    ## Examples

    ```
    Input: source = "abc", target = "abcbc"
    Output: 2
    Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
    ```

    ```
    Input: source = "abc", target = "acdbc"
    Output: -1
    Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
    ```

    ```
    Input: source = "xyz", target = "xzyxz"
    Output: 3
    Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
    ```

    ## Constraints

    - 1 <= source.length, target.length <= 1000
    - source and target consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shortest_way(self, source: str, target: str) -> int:
            raise NotImplementedError('Implement shortest_way')

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
