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
    # 3481. Apply Substitutions

    **Medium** · Depth-First Search, Breadth-First Search, Graph, Topological Sort, Array, Hash Table, String

    You are given a `replacements` mapping and a `text` string that may contain **placeholders** formatted as `%var%`, where each `var` corresponds to a key in the `replacements` mapping. Each replacement value may itself contain **one or more** such **placeholders**. Each **placeholder** is replaced by the value associated with its corresponding replacement key.

    Return the fully substituted `text` string which **does not** contain any **placeholders**.

    ## Examples

    ```
    Input: replacements = [["A","abc"],["B","def"]], text = "%A%_%B%"
    Output: "abc_def"
    Explanation: Replace %A% with "abc" and %B% with "def". The final text becomes "abc_def".
    ```

    ```
    Input: replacements = [["A","bce"],["B","ace"],["C","abc%B%"]], text = "%A%_%B%_%C%"
    Output: "bce_ace_abcace"
    Explanation: Replace %A% with "bce" and %B% with "ace". Then substitute %B% in "abc%B%" with "ace" to obtain "abcace". The final text becomes "bce_ace_abcace".
    ```

    ## Constraints

    - `1 <= replacements.length <= 10`
    - Each element of `replacements` is a two-element list `[key, value]`, where:
      - `key` is a single uppercase English letter.
      - `value` is a non-empty string of at most 8 characters that may contain zero or more placeholders formatted as `%<key>%`.
    - All replacement keys are unique.
    - The `text` string is formed by concatenating all key placeholders (formatted as `%<key>%`) randomly from the replacements mapping, separated by underscores.
    - `text.length == 4 * replacements.length - 1`
    - Every placeholder in the `text` or in any replacement value corresponds to a key in the `replacements` mapping.
    - There are no cyclic dependencies between replacement keys.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def apply_substitutions(self, replacements: list[list[str]], text: str) -> str:
            raise NotImplementedError('Implement apply_substitutions')

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
