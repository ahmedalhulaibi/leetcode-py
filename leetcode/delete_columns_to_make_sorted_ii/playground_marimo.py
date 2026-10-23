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
    # 955. Delete Columns to Make Sorted II

    **Medium** · Array, String, Greedy

    You are given an array of `n` strings `strs`, all of the same length.

    We may choose any deletion indices, and we delete all the characters in those indices for each string.

    For example, if we have `strs = ["abcdef","uvwxyz"]` and deletion indices `{0, 2, 3}`, then the final array after deletions is `["bef", "vyz"]`.

    Suppose we chose a set of deletion indices `answer` such that after deletions, the final array has its elements in **lexicographic** order (i.e., `strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]`). Return *the minimum possible value of* `answer.length`.

    ## Examples

    ```
    Input: strs = ["ca","bb","ac"]
    Output: 1
    Explanation: After deleting the first column, strs = ["a", "b", "c"]. Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]). We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.
    ```

    ```
    Input: strs = ["xc","yb","za"]
    Output: 0
    Explanation: strs is already in lexicographic order, so we do not need to delete anything.
    Note that the rows of strs are not necessarily in lexicographic order:
    i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)
    ```

    ```
    Input: strs = ["zyx","wvu","tsr"]
    Output: 3
    Explanation: We have to delete every column.
    ```

    ## Constraints

    - n == strs.length
    - 1 <= n <= 100
    - 1 <= strs[i].length <= 100
    - strs[i] consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_deletion_size(self, strs: list[str]) -> int:
            raise NotImplementedError('Implement min_deletion_size')

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
