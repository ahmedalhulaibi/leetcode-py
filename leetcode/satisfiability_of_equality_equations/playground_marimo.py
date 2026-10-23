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
    # 990. Satisfiability of Equality Equations

    **Medium** · Array, String, Union-Find, Graph Theory

    You are given an array of strings `equations` that represent relationships between variables where each string `equations[i]` is of length `4` and takes one of two different forms: `x<sub>i</sub>==y<sub>i</sub>` or `x<sub>i</sub>!=y<sub>i</sub>`. Here, `x<sub>i</sub>` and `y<sub>i</sub>` are lowercase letters (not necessarily different) that represent one-letter variable names.

    Return `true` if it is possible to assign integers to variable names so as to satisfy all the given equations, or `false` otherwise.

    ## Examples

    ```
    Input: equations = ["a==b","b!=a"]
    Output: false
    Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
    There is no way to assign the variables to satisfy both equations.
    ```

    ```
    Input: equations = ["b==a","a==b"]
    Output: true
    Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
    ```

    ## Constraints

    - 1 <= equations.length <= 500
    - equations[i].length == 4
    - equations[i][0] is a lowercase letter.
    - equations[i][1] is either '=' or '!'.
    - equations[i][2] is '='.
    - equations[i][3] is a lowercase letter.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def equations_possible(self, equations: list[str]) -> bool:
            raise NotImplementedError('Implement equations_possible')

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
