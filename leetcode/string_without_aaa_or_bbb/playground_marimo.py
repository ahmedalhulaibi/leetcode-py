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
    # 984. String Without AAA or BBB

    **Medium** · String, Greedy

    Given two integers `a` and `b`, return **any** string `s` such that:

    - `s` has length `a + b` and contains exactly `a` `'a'` letters, and exactly `b` `'b'` letters,
    - The substring `'aaa'` does not occur in `s`, and
    - The substring `'bbb'` does not occur in `s`.


    ## Examples

    ```
    Input: a = 1, b = 2
    Output: "abb"
    Explanation: "abb", "bab" and "bba" are all correct answers.
    ```

    ```
    Input: a = 4, b = 1
    Output: "aabaa"
    ```

    ## Constraints

    - `0 <= a, b <= 100`
    - It is guaranteed such an `s` exists for the given `a` and `b`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def str_without3a3b(self, a: int, b: int) -> str:
            raise NotImplementedError('Implement str_without3a3b')

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
