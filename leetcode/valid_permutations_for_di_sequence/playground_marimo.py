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
    # 903. Valid Permutations for DI Sequence

    **Hard** · String, Dynamic Programming, Prefix Sum

    You are given a string `s` of length `n` where `s[i]` is either:

    - `'D'` means decreasing, or
    - `'I'` means increasing.

    A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` is called a **valid permutation** if for all valid `i`:

    - If `s[i] == 'D'`, then `perm[i] > perm[i + 1]`, and
    - If `s[i] == 'I'`, then `perm[i] < perm[i + 1]`.

    Return *the number of **valid permutations*** `perm`. Since the answer may be large, return it **modulo** `10^9 + 7`.

    ## Examples

    ```
    Input: s = "DID"
    Output: 5
    ```
    **Explanation:** The 5 valid permutations of (0, 1, 2, 3) are:
    (1, 0, 3, 2)
    (2, 0, 3, 1)
    (2, 1, 3, 0)
    (3, 0, 2, 1)
    (3, 1, 2, 0)

    ```
    Input: s = "D"
    Output: 1
    ```

    ## Constraints

    - `n == s.length`
    - `1 <= n <= 200`
    - `s[i]` is either `'I'` or `'D'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_perms_di_sequence(self, s: str) -> int:
            raise NotImplementedError('Implement num_perms_di_sequence')

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
