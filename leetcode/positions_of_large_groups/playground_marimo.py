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
    # 830. Positions of Large Groups

    **Easy** · String

    In a string `s` of lowercase letters, these letters form consecutive groups of the same character.

    For example, a string like `s = "abbxxxxzyy"` has the groups `"a"`, `"bb"`, `"xxxx"`, `"z"`, and `"yy"`.

    A group is identified by an interval `[start, end]`, where `start` and `end` denote the start and end indices (inclusive) of the group. In the above example, `"xxxx"` has the interval `[3,6]`.

    A group is considered **large** if it has 3 or more characters.

    Return the intervals of every large group sorted in increasing order by start index.

    ## Examples

    ```
    Input: s = "abbxxxxzzy"
    Output: [[3,6]]
    Explanation: "xxxx" is the only large group with start index 3 and end index 6.
    ```

    ```
    Input: s = "abc"
    Output: []
    Explanation: We have groups "a", "b", and "c", none of which are large groups.
    ```

    ```
    Input: s = "abcdddeeeeaabbbcd"
    Output: [[3,5],[6,9],[12,14]]
    Explanation: The large groups are "ddd", "eeee", and "bbb".
    ```

    ## Constraints

    - 1 <= s.length <= 1000
    - s contains lowercase English letters only.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def large_group_positions(self, s: str) -> list[list[int]]:
            raise NotImplementedError('Implement large_group_positions')

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
