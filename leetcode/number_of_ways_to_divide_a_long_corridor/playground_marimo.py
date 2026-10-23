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
    # 2147. Number of Ways to Divide a Long Corridor

    **Hard** · Math, String, Dynamic Programming

    Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

    One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

    Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

    Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 10^9 + 7. If there is no way, return 0.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/12/04/1.png)

    ```
    Input: corridor = "SSPPSPS"
    Output: 3
    Explanation: There are 3 different ways to divide the corridor.
    The black bars in the above image indicate the two room dividers already installed.
    Note that in each of the ways, each section has exactly two seats.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/12/04/2.png)

    ```
    Input: corridor = "PPSPSP"
    Output: 1
    Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
    Installing any would create some section that does not have exactly two seats.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/12/12/3.png)

    ```
    Input: corridor = "S"
    Output: 0
    Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
    ```

    ## Constraints

    - n == corridor.length
    - 1 <= n <= 10^5
    - corridor[i] is either 'S' or 'P'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def number_of_ways(self, corridor: str) -> int:
            raise NotImplementedError('Implement number_of_ways')

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
