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
    # 2379. Minimum Recolors to Get K Consecutive Black Blocks

    **Easy** · String, Sliding Window

    You are given a 0-indexed string `blocks` of length `n`, where `blocks[i]` is either `'W'` or `'B'`, representing the color of the ith block. The characters `'W'` and `'B'` denote the colors white and black, respectively.

    You are also given an integer `k`, which is the desired number of consecutive black blocks.

    In one operation, you can recolor a white block such that it becomes a black block.

    Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

    ## Examples

    ```
    Input: blocks = "WBBWWBBWBW", k = 7
    Output: 3
    Explanation:
    One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
    so that blocks = "BBBBBBBWBW".
    It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
    Therefore, we return 3.
    ```

    ```
    Input: blocks = "WBWBBBW", k = 2
    Output: 0
    Explanation:
    No changes need to be made, since 2 consecutive black blocks already exist.
    Therefore, we return 0.
    ```

    ## Constraints

    - n == blocks.length
    - 1 <= n <= 100
    - blocks[i] is either 'W' or 'B'.
    - 1 <= k <= n



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_recolors(self, blocks: str, k: int) -> int:
            raise NotImplementedError('Implement minimum_recolors')

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
