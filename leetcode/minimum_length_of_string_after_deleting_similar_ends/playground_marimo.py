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
    # 1750. Minimum Length of String After Deleting Similar Ends

    **Medium** · Two Pointers, String

    <p>Given a string <code>s</code> consisting only of characters <code>'a'</code>, <code>'b'</code>, and <code>'c'</code>. You are asked to apply the following algorithm on the string any number of times:</p>

    <ol>
        <li>Pick a <strong>non-empty</strong> prefix from the string <code>s</code> where all the characters in the prefix are equal.</li>
        <li>Pick a <strong>non-empty</strong> suffix from the string <code>s</code> where all the characters in this suffix are equal.</li>
        <li>The prefix and the suffix should not intersect at any index.</li>
        <li>The characters from the prefix and suffix must be the same.</li>
        <li>Delete both the prefix and the suffix.</li>
    </ol>

    <p>Return <em>the <strong>minimum length</strong> of </em><code>s</code> <em>after performing the above operation any number of times (possibly zero times)</em>.</p>

    ## Examples

    ```
    Input: s = "ca"
    Output: 2
    ```
    **Explanation:** You can't remove any characters, so the string stays as is.

    ```
    Input: s = "cabaabac"
    Output: 0
    ```
    **Explanation:** An optimal sequence of operations is:
    - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
    - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
    - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
    - Take prefix = "a" and suffix = "a" and remove them, s = "\".

    ```
    Input: s = "aabccabba"
    Output: 3
    ```
    **Explanation:** An optimal sequence of operations is:
    - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
    - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

    ## Constraints

    - `1 <= s.length <= 10^5`
    - `s` consists only of characters `'a'`, `'b'`, and `'c'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_length(self, s: str) -> int:
            raise NotImplementedError('Implement minimum_length')

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
