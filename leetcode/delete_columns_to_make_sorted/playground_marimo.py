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
    # 944. Delete Columns to Make Sorted

    **Easy** · Array, String, Greedy

    You are given an array of `n` strings `strs`, all of the same length.

    The strings can be arranged such that there is one on each line, making a grid.

    - For example, `strs = ["abc", "bce", "cae"]` can be arranged as follows:

    ```
    abc
    bce
    cae
    ```

    You want to **delete** the columns that are **not sorted lexicographically**. In the above example (**0-indexed**), columns 0 (`'a'`, `'b'`, `'c'`) and 2 (`'c'`, `'e'`, `'e'`) are sorted, while column 1 (`'b'`, `'c'`, `'a'`) is not, so you would delete column 1.

    Return *the number of columns that you will delete*.

    ## Examples

    ```
    Input: strs = ["cba","daf","ghi"]
    Output: 1
    Explanation: The grid looks as follows:
      cba
      daf
      ghi
    Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
    ```

    ```
    Input: strs = ["a","b"]
    Output: 0
    Explanation: The grid looks as follows:
      a
      b
    Column 0 is the only column and is sorted, so you will not delete any columns.
    ```

    ```
    Input: strs = ["zyx","wvu","tsr"]
    Output: 3
    Explanation: The grid looks as follows:
      zyx
      wvu
      tsr
    All 3 columns are not sorted, so you will delete all 3.
    ```

    ## Constraints

    - n == strs.length
    - 1 <= n <= 100
    - 1 <= strs[i].length <= 1000
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
