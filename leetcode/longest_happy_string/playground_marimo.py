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
    # 1405. Longest Happy String

    **Medium** · String, Greedy, Heap (Priority Queue)

    A string `s` is called **happy** if it satisfies the following conditions:

    - `s` only contains the letters `'a'`, `'b'`, and `'c'`.
    - `s` does not contain any of `"aaa"`, `"bbb"`, or `"ccc"` as a substring.
    - `s` contains **at most** `a` occurrences of the letter `'a'`.
    - `s` contains **at most** `b` occurrences of the letter `'b'`.
    - `s` contains **at most** `c` occurrences of the letter `'c'`.

    Given three integers `a`, `b`, and `c`, return *the **longest possible happy** string*. If there are multiple longest happy strings, return *any of them*. If there is no such string, return *the empty string* `"\"`.

    ## Examples

    ```
    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.
    ```

    ```
    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    Explanation: It is the only correct answer in this case.
    ```

    ## Constraints

    - `0 <= a, b, c <= 100`
    - `a + b + c > 0`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def longest_happy_string(self, a: int, b: int, c: int) -> str:
            raise NotImplementedError('Implement longest_happy_string')

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
