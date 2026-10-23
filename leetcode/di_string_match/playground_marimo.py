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
    # 942. DI String Match

    **Easy** · Array, Two Pointers, String, Greedy

    A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

    - `s[i] == 'I'` if `perm[i] < perm[i + 1]`, and
    - `s[i] == 'D'` if `perm[i] > perm[i + 1]`.

    Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid permutations `perm`, return **any of them**.

    ## Examples

    ```
    Input: s = "IDID"
    Output: [0,4,1,3,2]
    Explanation: [0,4,1,3,2] is one valid answer.
    ```

    ```
    Input: s = "III"
    Output: [0,1,2,3]
    ```

    ```
    Input: s = "DDI"
    Output: [3,2,0,1]
    ```

    ## Constraints

    - `1 <= s.length <= 10^5`
    - `s[i]` is either `'I'` or `'D'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def di_string_match(self, s: str) -> list[int]:
            raise NotImplementedError('Implement di_string_match')

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
