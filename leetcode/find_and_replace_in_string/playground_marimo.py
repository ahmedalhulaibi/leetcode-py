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
    # 833. Find And Replace in String

    **Medium** · Array, Hash Table, String, Sorting

    You are given a 0-indexed string `s` that you must perform `k` replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, `indices`, `sources`, and `targets`, all of length `k`.

    To complete the `ith` replacement operation:

    - Check if the substring `sources[i]` occurs at index `indices[i]` in the original string `s`.
    - If it does not occur, do nothing.
    - Otherwise if it does occur, replace that substring with `targets[i]`.

    For example, if `s = "abcd"`, `indices[i] = 0`, `sources[i] = "ab"`, and `targets[i] = "eee"`, then the result of this replacement will be `"eeecd"`.

    All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

    - For example, a testcase with `s = "abc"`, `indices = [0, 1]`, and `sources = ["ab","bc"]` will not be generated because the `"ab"` and `"bc"` replacements overlap.

    Return the resulting string after performing all replacement operations on `s`.

    A substring is a contiguous sequence of characters in a string.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png)

    ```
    Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
    Output: "eeebffff"
    Explanation:
    "a" occurs at index 0 in s, so we replace it with "eee".
    "cd" occurs at index 2 in s, so we replace it with "ffff".
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/06/12/833-ex2-1.png)

    ```
    Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
    Output: "eeecd"
    Explanation:
    "ab" occurs at index 0 in s, so we replace it with "eee".
    "ec" does not occur at index 2 in s, so we do nothing.
    ```

    ## Constraints

    - 1 <= s.length <= 1000
    - k == indices.length == sources.length == targets.length
    - 1 <= k <= 100
    - 0 <= indices[i] < s.length
    - 1 <= sources[i].length, targets[i].length <= 50
    - s consists of only lowercase English letters.
    - sources[i] and targets[i] consist of only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_replace_string(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
            raise NotImplementedError('Implement find_replace_string')

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
