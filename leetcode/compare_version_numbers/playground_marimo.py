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
    # 165. Compare Version Numbers

    **Medium** · Two Pointers, String

    Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots `'.'`. The value of the revision is its integer conversion ignoring leading zeros.

    To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

    Return the following:

    - If version1 < version2, return -1.
    - If version1 > version2, return 1.
    - Otherwise, return 0.

    ## Examples

    ```
    Input: version1 = "1.2", version2 = "1.10"
    Output: -1
    Explanation:
    version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.
    ```

    ```
    Input: version1 = "1.01", version2 = "1.001"
    Output: 0
    Explanation:
    Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
    ```

    ```
    Input: version1 = "1.0", version2 = "1.0.0.0"
    Output: 0
    Explanation:
    version1 has less revisions, which means every missing revision are treated as "0".
    ```

    ## Constraints

    - `1 <= version1.length, version2.length <= 500`
    - `version1` and `version2` only contain digits and `'.'`.
    - `version1` and `version2` are valid version numbers.
    - All the given revisions in `version1` and `version2` can be stored in a 32-bit integer.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def compare_version(self, version1: str, version2: str) -> int:
            raise NotImplementedError('Implement compare_version')

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
