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
    # 1079. Letter Tile Possibilities

    **Medium** · Hash Table, String, Backtracking, Counting

    You have <code>n</code>&nbsp;&nbsp;<code>tiles</code>, where each tile has one letter <code>tiles[i]</code> printed on it.

    Return <em>the number of possible non-empty sequences of letters</em> you can make using the letters printed on those <code>tiles</code>.

    ## Examples

    ```
    Input: tiles = "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
    ```

    ```
    Input: tiles = "AAABBC"
    Output: 188
    ```

    ```
    Input: tiles = "V"
    Output: 1
    ```

    ## Constraints

    - <code>1 &lt;= tiles.length &lt;= 7</code>
    - <code>tiles</code> consists of uppercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_tile_possibilities(self, tiles: str) -> int:
            raise NotImplementedError('Implement num_tile_possibilities')

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
