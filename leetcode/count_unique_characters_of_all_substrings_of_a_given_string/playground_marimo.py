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
    mo.md(r"""
    # 828. Count Unique Characters of All Substrings of a Given String

    **Hard** · Hash Table, String, Dynamic Programming

    <p>Let's define a function <code>countUniqueChars(s)</code> that returns the number of unique characters in <code>s</code>.</p>

    <ul>
        <li>For example, calling <code>countUniqueChars(s)</code> if <code>s = "LEETCODE"</code> then <code>"L"</code>, <code>"T"</code>, <code>"C"</code>, <code>"O"</code>, <code>"D"</code> are the unique characters since they appear only once in <code>s</code>, therefore <code>countUniqueChars(s) = 5</code>.</li>
    </ul>

    <p>Given a string <code>s</code>, return the sum of <code>countUniqueChars(t)</code> where <code>t</code> is a substring of <code>s</code>. The test cases are generated such that the answer fits in a 32-bit integer.</p>

    <p>Notice that some substrings can be repeated so in this case you have to count the repeated ones too.</p>

    ## Examples

    ```
    Input: s = "ABC"
    Output: 10
    Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
    Every substring is composed with only unique letters.
    Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
    ```

    ```
    Input: s = "ABA"
    Output: 8
    Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
    ```

    ```
    Input: s = "LEETCODE"
    Output: 92
    ```

    ## Constraints

    - 1 <= s.length <= 10^5
    - s consists of uppercase English letters only.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def unique_letter_string(self, s: str) -> int:
            raise NotImplementedError('Implement unique_letter_string')

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
