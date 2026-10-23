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
    # 2109. Adding Spaces to a String

    **Medium** · Array, Two Pointers, String, Simulation

    You are given a **0-indexed** string `s` and a **0-indexed** integer array `spaces` that describes the indices in the original string where spaces will be added. Each space should be inserted **before** the character at the given index.

    - For example, given `s = "EnjoyYourCoffee"` and `spaces = [5, 9]`, we place spaces before `'Y'` and `'C'`, which are at indices `5` and `9` respectively. Thus, we obtain `"Enjoy Your Coffee"`.

    Return the modified string after the spaces have been added.

    ## Examples

    ```
    Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
    Output: "Leetcode Helps Me Learn"
    ```
    **Explanation:** The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn". We then place spaces before those characters.

    ```
    Input: s = "icodeinpython", spaces = [1,5,7,9]
    Output: "i code in py thon"
    ```
    **Explanation:** The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython". We then place spaces before those characters.

    ```
    Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
    Output: " s p a c i n g"
    ```
    **Explanation:** We are also able to place spaces before the first character of the string.

    ## Constraints

    - `1 <= s.length <= 3 * 10^5`
    - `s` consists only of lowercase and uppercase English letters.
    - `1 <= spaces.length <= 3 * 10^5`
    - `0 <= spaces[i] <= s.length - 1`
    - All the values of `spaces` are **strictly increasing**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def add_spaces(self, s: str, spaces: list[int]) -> str:
            raise NotImplementedError('Implement add_spaces')

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
