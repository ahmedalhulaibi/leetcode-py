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
    # 947. Most Stones Removed with Same Row or Column

    **Medium** · Hash Table, Depth-First Search, Union-Find, Graph Theory, Bipartite Graph

    On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

    A stone can be removed if it shares either **the same row or the same column** as another stone that has not been removed.

    Given an array `stones` of length `n` where `stones[i] = [x<sub>i</sub>, y<sub>i</sub>]` represents the location of the `i<sup>th</sup>` stone, return _the largest possible number of stones that can be removed_.

    ## Examples

    ```
    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5
    ```

    ```
    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3
    ```

    ```
    Input: stones = [[0,0]]
    Output: 0
    ```

    ## Constraints

    - 1 <= stones.length <= 1000
    - 0 <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>4</sup>
    - No two stones are at the same coordinate point.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def remove_stones(self, stones: list[list[int]]) -> int:
            raise NotImplementedError('Implement remove_stones')

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
