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
    # 899. Orderly Queue

    **Hard** · Math, String, Sorting, Lexicographically Minimal String Rotation

    You are given a string `s` and an integer `k`. You can choose one of the first `k` letters of `s` and append it at the end of the string.

    Return *the lexicographically smallest string you could have after applying the mentioned step any number of moves*.

    ## Examples

    ```
    Input: s = "cba", k = 1
    Output: "acb"
    Explanation: In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
    In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
    ```

    ```
    Input: s = "baaca", k = 3
    Output: "aaabc"
    Explanation: In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
    In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
    ```

    ## Constraints

    - `1 <= k <= s.length <= 1000`
    - `s` consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def orderly_queue(self, s: str, k: int) -> str:
            raise NotImplementedError('Implement orderly_queue')

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
