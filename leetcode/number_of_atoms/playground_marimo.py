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
    # 726. Number of Atoms

    **Hard** · Hash Table, String, Stack, Sorting

    Given a string `formula` representing a chemical formula, return the count of each atom.

    The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

    One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

    - For example, `"H2O"` and `"H2O2"` are possible, but `"H1O2"` is impossible.

    Two formulas are concatenated together to produce another formula.

    - For example, `"H2O2He3Mg4"` is also a formula.

    A formula placed in parentheses, and a count (optionally added) is also a formula.

    - For example, `"(H2O2)"` and `"(H2O2)3"` are formulas.

    Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

    The test cases are generated so that all the values in the output fit in a 32-bit integer.

    ## Examples

    ```
    Input: formula = "H2O"
    Output: "H2O"
    Explanation: The count of elements are {'H': 2, 'O': 1}.
    ```

    ```
    Input: formula = "Mg(OH)2"
    Output: "H2MgO2"
    Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
    ```

    ```
    Input: formula = "K4(ON(SO3)2)2"
    Output: "K4N2O14S4"
    Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
    ```

    ## Constraints

    - 1 <= formula.length <= 1000
    - formula consists of English letters, digits, '(', and ')'.
    - formula is always valid.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import re
    from collections import Counter

    class Solution:

        def count_of_atoms(self, formula: str) -> str:
            raise NotImplementedError('Implement count_of_atoms')

    practice_exports = {'re': re, 'Counter': Counter, 'Solution': Solution}
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
