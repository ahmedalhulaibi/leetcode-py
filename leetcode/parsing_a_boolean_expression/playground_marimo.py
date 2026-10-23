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
    # 1106. Parsing A Boolean Expression

    **Hard** · String, Stack, Recursion

    A <strong>boolean expression</strong> is an expression that evaluates to either <code>true</code> or <code>false</code>. It can be in one of the following shapes:

    - <code>&#39;t&#39;</code> that evaluates to <code>true</code>.
    - <code>&#39;f&#39;</code> that evaluates to <code>false</code>.
    - <code>&#39;!(subExpr)&#39;</code> that evaluates to <strong>the logical NOT</strong> of the inner expression <code>subExpr</code>.
    - <code>&#39;&amp;(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)&#39;</code> that evaluates to <strong>the logical AND</strong> of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where <code>n &gt;= 1</code>.
    - <code>&#39;|(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)&#39;</code> that evaluates to <strong>the logical OR</strong> of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where <code>n &gt;= 1</code>.

    Given a string <code>expression</code> that represents a <strong>boolean expression</strong>, return <em>the evaluation of that expression</em>.

    It is <strong>guaranteed</strong> that the given expression is valid and follows the given rules.

    ## Examples

    ```
    Input: expression = "&(|(f))"
    Output: false
    Explanation: First, evaluate |(f) --> f. The expression is now "&(f)". Then, evaluate &(f) --> f. The expression is now "f". Finally, return false.
    ```

    ```
    Input: expression = "|(f,f,f,t)"
    Output: true
    Explanation: The evaluation of (false OR false OR false OR true) is true.
    ```

    ```
    Input: expression = "!(&(f,t))"
    Output: true
    Explanation: First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)". Then, evaluate !(f) --> NOT false --> true. We return true.
    ```

    ## Constraints

    - <code>1 &lt;= expression.length &lt;= 2 * 10<sup>4</sup></code>
    - <code>expression[i]</code> is one following characters: <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;&amp;&#39;</code>, <code>&#39;|&#39;</code>, <code>&#39;!&#39;</code>, <code>&#39;t&#39;</code>, <code>&#39;f&#39;</code>, and <code>&#39;,&#39;</code>.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def parse_bool_expr(self, expression: str) -> bool:
            raise NotImplementedError('Implement parse_bool_expr')

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
