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
    # 2375. Construct Smallest Number From DI String

    **Medium** · String, Backtracking, Stack, Greedy

    You are given a 0-indexed string `pattern` of length `n` consisting of the characters `'I'` meaning increasing and `'D'` meaning decreasing.

    A 0-indexed string `num` of length `n + 1` is created using the following conditions:

    - `num` consists of the digits `'1'` to `'9'`, where each digit is used at most once.
    - If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.
    - If `pattern[i] == 'D'`, then `num[i] > num[i + 1]`.

    Return the lexicographically smallest possible string `num` that meets the conditions.

    ## Examples

    ```
    Input: pattern = "IIIDIDDD"
    Output: "123549876"
    Explanation:
    At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
    At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
    Some possible values of num are "245639871", "135749862", and "123849765".
    It can be proven that "123549876" is the smallest possible num that meets the conditions.
    ```

    ```
    Input: pattern = "DDD"
    Output: "4321"
    Explanation:
    Some possible values of num are "9876", "7321", and "8742".
    It can be proven that "4321" is the smallest possible num that meets the conditions.
    ```

    ## Constraints

    - 1 <= pattern.length <= 8
    - pattern consists of only the letters 'I' and 'D'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def smallest_number(self, pattern: str) -> str:
            raise NotImplementedError('Implement smallest_number')

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
