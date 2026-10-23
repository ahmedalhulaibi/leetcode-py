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
    # 936. Stamping The Sequence

    **Hard** · String, Stack, Greedy, Queue

    You are given two strings `stamp` and `target`. Initially, there is a string `s` of length `target.length` with all `s[i] == '?'`.

    In one turn, you can place `stamp` over `s` and replace every letter in the `s` with the corresponding letter from `stamp`.

    - For example, if `stamp = "abc"` and `target = "abcba"`, then `s` is `"?????"` initially. In one turn you can:
      - place `stamp` at index `0` of `s` to obtain `"abc??"`,
      - place `stamp` at index `1` of `s` to obtain `"?abc?"`, or
      - place `stamp` at index `2` of `s` to obtain `"??abc"`.

      Note that `stamp` must be fully contained in the boundaries of `s` in order to stamp (i.e., you cannot place `stamp` at index `3` of `s`).

    We want to convert `s` to `target` using **at most** `10 * target.length` turns.

    Return *an array of the index of the left-most letter being stamped at each turn*. If we cannot obtain `target` from `s` within `10 * target.length` turns, return an empty array.

    ## Examples

    ```
    Input: stamp = "abc", target = "ababc"
    Output: [0,2]
    Explanation: Initially s = "?????".
    - Place stamp at index 0 to get "abc??".
    - Place stamp at index 2 to get "ababc".
    [1,0,2] would also be accepted as an answer, as well as some other answers.
    ```

    ```
    Input: stamp = "abca", target = "aabcaca"
    Output: [3,0,1]
    Explanation: Initially s = "???????".
    - Place stamp at index 3 to get "???abca".
    - Place stamp at index 0 to get "abcabca".
    - Place stamp at index 1 to get "aabcaca".
    ```

    ## Constraints

    - `1 <= stamp.length <= target.length <= 1000`
    - `stamp` and `target` consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def moves_to_stamp(self, stamp: str, target: str) -> list[int]:
            raise NotImplementedError('Implement moves_to_stamp')

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
