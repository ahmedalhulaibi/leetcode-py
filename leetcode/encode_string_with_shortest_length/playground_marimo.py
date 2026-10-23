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
    # 471. Encode String with Shortest Length

    **Hard** · String, Dynamic Programming

    Given a string `s`, encode the string such that its encoded length is the shortest.

    The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. `k` should be a positive integer.

    If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return **any of them**.

    ## Examples

    ```
    Input: s = "aaa"
    Output: "aaa"
    Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
    ```

    ```
    Input: s = "aaaaa"
    Output: "5[a]"
    Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
    ```

    ```
    Input: s = "aaaaaaaaaa"
    Output: "10[a]"
    Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
    ```

    ## Constraints

    - `1 <= s.length <= 150`
    - `s` consists of only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def encode(self, s: str) -> str:
            raise NotImplementedError('Implement encode')

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
