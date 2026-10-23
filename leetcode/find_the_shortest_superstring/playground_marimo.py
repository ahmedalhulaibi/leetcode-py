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
    # 943. Find the Shortest Superstring

    **Hard** · Array, String, Dynamic Programming, Bit Manipulation, Bitmask, Hamiltonian Path

    Given an array of strings `words`, return *the smallest string that contains each string in* `words` *as a substring*. If there are multiple valid strings of the smallest length, return **any of them**.

    You may assume that no string in `words` is a substring of another string in `words`.

    ## Examples

    ```
    Input: words = ["alex","loves","leetcode"]
    Output: "alexlovesleetcode"
    Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
    ```

    ```
    Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    Output: "gctaagttcatgcatc"
    ```

    ## Constraints

    - `1 <= words.length <= 12`
    - `1 <= words[i].length <= 20`
    - `words[i]` consists of lowercase English letters.
    - All the strings of `words` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shortest_superstring(self, words: list[str]) -> str:
            raise NotImplementedError('Implement shortest_superstring')

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
