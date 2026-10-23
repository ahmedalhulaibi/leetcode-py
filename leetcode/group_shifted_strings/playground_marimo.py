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
    # 249. Group Shifted Strings

    **Medium** · Array, Hash Table, String

    Perform the following shift operations on a string:

    - **Right shift**: Replace every letter with the **successive** letter of the English alphabet, where `'z'` is replaced by `'a'`. For example, `"abc"` can be right-shifted to `"bcd"` or `"xyz"` can be right-shifted to `"yza"`.
    - **Left shift**: Replace every letter with the **preceding** letter of the English alphabet, where `'a'` is replaced by `'z'`. For example, `"bcd"` can be left-shifted to `"abc"` or `"yza"` can be left-shifted to `"xyz"`.

    We can keep shifting the string in both directions to form an **endless** **shifting sequence**.

    - For example, shift `"abc"` to form the sequence: `... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> ...` `<-> "zab" <-> "abc" <-> ...`.

    You are given an array of strings `strings`, group together all `strings[i]` that belong to the same shifting sequence. You may return the answer in **any order**.

    ## Examples

    ```
    Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
    Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    ```

    ```
    Input: strings = ["a"]
    Output: [["a"]]
    ```

    ## Constraints

    - `1 <= strings.length <= 200`
    - `1 <= strings[i].length <= 50`
    - `strings[i]` consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import defaultdict

    class Solution:

        def group_strings(self, strings: list[str]) -> list[list[str]]:
            raise NotImplementedError('Implement group_strings')

    practice_exports = {'defaultdict': defaultdict, 'Solution': Solution}
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
