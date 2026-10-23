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
    # 756. Pyramid Transition Matrix

    **Medium** · Hash Table, String, Backtracking, Bit Manipulation

    You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains **one less block** than the row beneath it and is centered on top.

    To make the pyramid aesthetically pleasing, there are only specific **triangular patterns** that are allowed. A triangular pattern consists of a **single block** stacked on top of **two blocks**. The patterns are given as a list of three-letter strings `allowed`, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

    - For example, `"ABC"` represents a triangular pattern with a `'C'` block stacked on top of an `'A'` (left) and `'B'` (right) block. Note that this is different from `"BAC"` where `'B'` is on the left bottom and `'A'` is on the right bottom.

    You start with a bottom row of blocks `bottom`, given as a single string, that you **must** use as the base of the pyramid.

    Given `bottom` and `allowed`, return `true` if you can build the pyramid all the way to the top such that **every triangular pattern** in the pyramid is in `allowed`, or `false` otherwise.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/08/26/pyramid1-grid.jpg)

    ```
    Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
    Output: true
    ```
    **Explanation:** The allowed triangular patterns are shown on the right.
    Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
    There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.

    ![Example 2](https://assets.leetcode.com/uploads/2021/08/26/pyramid2-grid.jpg)

    ```
    Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
    Output: false
    ```
    **Explanation:** The allowed triangular patterns are shown on the right.
    Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.

    ## Constraints

    - `2 <= bottom.length <= 6`
    - `0 <= allowed.length <= 216`
    - `allowed[i].length == 3`
    - The letters in all input strings are from the set `{'A', 'B', 'C', 'D', 'E', 'F'}`.
    - All the values of `allowed` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def pyramid_transition(self, bottom: str, allowed: list[str]) -> bool:
            raise NotImplementedError('Implement pyramid_transition')

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
