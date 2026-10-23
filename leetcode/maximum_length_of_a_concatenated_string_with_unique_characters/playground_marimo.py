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
    # 1239. Maximum Length of a Concatenated String with Unique Characters

    **Medium** · Array, String, Backtracking, Bit Manipulation

    You are given an array of strings `arr`. A string `s` is formed by the **concatenation** of a **subsequence** of `arr` that has **unique characters**.

    Return *the **maximum** possible length* of `s`.

    A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

    ## Examples

    ```
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All the valid concatenations are:
    - "\"
    - "un"
    - "iq"
    - "ue"
    - "uniq" ("un" + "iq")
    - "ique" ("iq" + "ue")
    Maximum length is 4.
    ```

    ```
    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
    ```

    ```
    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
    Explanation: The only string in arr has all 26 characters.
    ```

    ## Constraints

    - `1 <= arr.length <= 16`
    - `1 <= arr[i].length <= 26`
    - `arr[i]` contains only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_len(self, arr: list[str]) -> int:
            raise NotImplementedError('Implement max_len')

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
