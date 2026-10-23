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
    # 921. Minimum Add to Make Parentheses Valid

    **Medium** · String, Stack, Greedy

    <p>A parentheses string is valid if and only if:</p>

    <ul>
        <li>It is the empty string,</li>
        <li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
        <li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
    </ul>

    <p>You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.</p>

    <ul>
        <li>For example, if <code>s = &quot;()))&quot;</code>, you can insert an opening parenthesis to be <code>&quot;(()))&quot;</code> or a closing parenthesis to be <code>&quot;())))&quot;</code>.</li>
    </ul>

    <p>Return <em>the minimum number of moves required to make </em><code>s</code><em> valid</em>.</p>

    ## Examples

    ```
    Input: s = "())"
    Output: 1
    ```

    ```
    Input: s = "((("
    Output: 3
    ```

    ## Constraints

    - 1 &lt;= s.length &lt;= 1000
    - s[i] is either &#39;(&#39; or &#39;)&#39;.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_add_to_make_valid(self, s: str) -> int:
            raise NotImplementedError('Implement min_add_to_make_valid')

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
