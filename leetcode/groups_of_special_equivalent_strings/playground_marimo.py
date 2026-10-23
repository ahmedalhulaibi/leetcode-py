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
    # 893. Groups of Special-Equivalent Strings

    **Medium** · Array, Hash Table, String, Sorting

    You are given an array of strings of the same length `words`.

    In one **move**, you can swap any two even indexed characters or any two odd indexed characters of a string `words[i]`.

    Two strings `words[i]` and `words[j]` are **special-equivalent** if after any number of moves, `words[i] == words[j]`.

    - For example, `words[i] = "zzxy"` and `words[j] = "xyzz"` are **special-equivalent** because we may make the moves `"zzxy" -> "xzzy" -> "xyzz"`.

    A **group of special-equivalent strings** from `words` is a non-empty subset of words such that:

    - Every pair of strings in the group are special equivalent, and
    - The group is the largest size possible (i.e., there is not a string `words[i]` not in the group such that `words[i]` is special-equivalent to every string in the group).

    Return *the number of **groups of special-equivalent strings** from* `words`.

    ## Examples

    ```
    Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
    Output: 3
    Explanation:
    One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings is all pairwise special equivalent to these.
    The other two groups are ["xyzz", "zzxy"] and ["zzyx"].
    Note that in particular, "zzxy" is not special equivalent to "zzyx".
    ```

    ```
    Input: words = ["abc","acb","bac","bca","cab","cba"]
    Output: 3
    ```

    ## Constraints

    - 1 <= words.length <= 1000
    - 1 <= words[i].length <= 20
    - words[i] consist of lowercase English letters.
    - All the strings are of the same length.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_special_equivalent_groups(self, words: list[str]) -> int:
            raise NotImplementedError('Implement num_special_equivalent_groups')

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
