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
    # 1639. Number of Ways to Form a Target String Given a Dictionary

    **Hard** · Array, String, Dynamic Programming

    You are given a list of strings of the same length `words` and a string `target`.

    Your task is to form `target` using the given `words` under the following rules:

    - `target` should be formed from left to right.
    - To form the `i`th character (0-indexed) of `target`, you can choose the `k`th character of the `j`th string in `words` if `target[i] = words[j][k]`.
    - Once you use the `k`th character of the `j`th string of `words`, you can no longer use the `x`th character of any string in `words` where `x <= k`. In other words, all characters to the left of or at index `k` become unusuable for every string.
    - Repeat the process until you form the string `target`.

    Notice that you can use multiple characters from the same string in `words` provided the conditions above are met.

    Return the number of ways to form `target` from `words`. Since the answer may be too large, return it modulo `10^9 + 7`.

    ## Examples

    ```
    Input: words = ["acca","bbbb","caca"], target = "aba"
    Output: 6
    Explanation: There are 6 ways to form target.
    - index 0 (acca), index 1 (bbbb), index 3 (caca)
    - index 0 (acca), index 2 (bbbb), index 3 (caca)
    - index 0 (acca), index 1 (bbbb), index 3 (acca)
    - index 0 (acca), index 2 (bbbb), index 3 (acca)
    - index 1 (caca), index 2 (bbbb), index 3 (acca)
    - index 1 (caca), index 2 (bbbb), index 3 (caca)
    ```

    ```
    Input: words = ["abba","baab"], target = "bab"
    Output: 4
    Explanation: There are 4 ways to form target.
    - index 0 (baab), index 1 (baab), index 2 (abba)
    - index 0 (baab), index 1 (baab), index 3 (baab)
    - index 0 (baab), index 2 (baab), index 3 (baab)
    - index 1 (abba), index 2 (baab), index 3 (baab)
    ```

    ## Constraints

    - 1 <= words.length <= 1000
    - 1 <= words[i].length <= 1000
    - All strings in `words` have the same length.
    - 1 <= target.length <= 1000
    - `words[i]` and `target` consist of only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_ways(self, words: list[str], target: str) -> int:
            raise NotImplementedError('Implement num_ways')

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
