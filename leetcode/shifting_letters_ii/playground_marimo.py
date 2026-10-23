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
    # 2381. Shifting Letters II

    **Medium** · Array, String, Prefix Sum

    You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [start<sub>i</sub>, end<sub>i</sub>, direction<sub>i</sub>]`. For every `i`, **shift** the characters in `s` from the index `start<sub>i</sub>` to the index `end<sub>i</sub>` (**inclusive**) forward if `direction<sub>i</sub> = 1`, or shift the characters backward if `direction<sub>i</sub> = 0`.

    Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

    Return *the final string after all such shifts to* `s` *are applied*.

    ## Examples

    ```
    Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
    Output: "ace"
    Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
    Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
    Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
    ```

    ```
    Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
    Output: "catz"
    Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
    Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
    ```

    ## Constraints

    - `1 <= s.length, shifts.length <= 5 * 10^4`
    - `shifts[i].length == 3`
    - `0 <= start_i <= end_i < s.length`
    - `0 <= direction_i <= 1`
    - `s` consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shifting_letters(self, s: str, shifts: list[list[int]]) -> str:
            raise NotImplementedError('Implement shifting_letters')

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
