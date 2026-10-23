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
    # 1891. Cutting Ribbons

    **Medium** · Array, Binary Search

    You are given an integer array `ribbons`, where `ribbons[i]` represents the length of the i<sup>th</sup> ribbon, and an integer `k`. You may cut any of the ribbons into any number of segments of **positive integer** lengths, or perform no cuts at all.

    - For example, if you have a ribbon of length `4`, you can:
      - Keep the ribbon of length `4`,
      - Cut it into one ribbon of length `3` and one ribbon of length `1`,
      - Cut it into two ribbons of length `2`,
      - Cut it into one ribbon of length `2` and two ribbons of length `1`, or
      - Cut it into four ribbons of length `1`.

    Your task is to determine the **maximum** length of ribbon, `x`, that allows you to cut _at least_ `k` ribbons, each of length `x`. You can discard any leftover ribbon from the cuts. If it is **impossible** to cut `k` ribbons of the same length, return 0.

    ## Examples

    ```
    Input: ribbons = [9,7,5], k = 3
    Output: 5
    Explanation:
    - Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
    - Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
    - Keep the third ribbon as it is.
    Now you have 3 ribbons of length 5.
    ```

    ```
    Input: ribbons = [7,5,9], k = 4
    Output: 4
    Explanation:
    - Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
    - Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
    - Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
    Now you have 4 ribbons of length 4.
    ```

    ```
    Input: ribbons = [5,7,9], k = 22
    Output: 0
    Explanation: You cannot obtain k ribbons of the same positive integer length.
    ```

    ## Constraints

    - 1 <= ribbons.length <= 10<sup>5</sup>
    - 1 <= ribbons[i] <= 10<sup>5</sup>
    - 1 <= k <= 10<sup>9</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_length(self, ribbons: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_length')

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
