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
    # 1871. Jump Game VII

    **Medium** · String, Dynamic Programming, Sliding Window, Prefix Sum

    You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

    - `i + minJump <= j <= min(i + maxJump, s.length - 1)`, and
    - `s[j] == '0'`.

    Return `true` *if you can reach index* `s.length - 1` *in* `s`, or `false` otherwise.

    ## Examples

    ```
    Input: s = "011010", minJump = 2, maxJump = 3
    Output: true
    Explanation:
    In the first step, move from index 0 to index 3.
    In the second step, move from index 3 to index 5.
    ```

    ```
    Input: s = "01101110", minJump = 2, maxJump = 3
    Output: false
    ```

    ## Constraints

    - 2 <= s.length <= 10^5
    - s[i] is either '0' or '1'.
    - s[0] == '0'
    - 1 <= minJump <= maxJump < s.length



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_reach(self, s: str, min_jump: int, max_jump: int) -> bool:
            raise NotImplementedError('Implement can_reach')

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
