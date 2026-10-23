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
    # 2275. Largest Combination With Bitwise AND Greater Than Zero

    **Medium** · Array, Hash Table, Bit Manipulation, Counting

    The **bitwise AND** of an array `nums` is the bitwise AND of all integers in `nums`.

    - For example, for `nums = [1, 5, 3]`, the bitwise AND is equal to `1 & 5 & 3 = 1`.
    - Also, for `nums = [7]`, the bitwise AND is `7`.

    You are given an array of positive integers `candidates`. Compute the **bitwise AND** for all possible **combinations** of elements in the `candidates` array.

    Return *the size of the **largest** combination of* `candidates` *with a bitwise AND* ***greater*** *than* `0`.

    ## Examples

    ```
    Input: candidates = [16,17,71,62,12,24,14]
    Output: 4
    ```
    **Explanation:** The combination `[16,17,62,24]` has a bitwise AND of `16 & 17 & 62 & 24 = 16 > 0`. The size of the combination is 4.
    It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0. Note that more than one combination may have the largest size.
    For example, the combination `[62,12,24,14]` has a bitwise AND of `62 & 12 & 24 & 14 = 8 > 0`.

    ```
    Input: candidates = [8,8]
    Output: 2
    ```
    **Explanation:** The largest combination `[8,8]` has a bitwise AND of `8 & 8 = 8 > 0`. The size of the combination is 2, so we return 2.

    ## Constraints

    - `1 <= candidates.length <= 10^5`
    - `1 <= candidates[i] <= 10^7`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def largest_combination(self, candidates: list[int]) -> int:
            raise NotImplementedError('Implement largest_combination')

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
