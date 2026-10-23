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
    # 2125. Number of Laser Beams in a Bank

    **Medium** · Array, Math, String, Matrix

    Anti-theft security devices are activated inside a bank. You are given a **0-indexed** binary string array `bank` representing the floor plan of the bank, which is an `m x n` 2D matrix. `bank[i]` represents the `ith` row, consisting of `'0'`s and `'1'`s. `'0'` means the cell is empty, while `'1'` means the cell has a security device.

    There is **one** laser beam between any **two** security devices **if both** conditions are met:

    - The two devices are located on two **different rows**: `r1` and `r2`, where `r1 < r2`.
    - For **each** row `i` where `r1 < i < r2`, there are **no security devices** in the `ith` row.

    Laser beams are independent, i.e., one beam does not interfere nor join with another.

    Return *the total number of laser beams in the bank*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg)

    ```
    Input: bank = ["011001","000000","010100","001000"]
    Output: 8
    ```
    **Explanation:** Between each of the following device pairs, there is one beam. In total, there are 8 beams:

    - bank[0][1] -- bank[2][1]
    - bank[0][1] -- bank[2][3]
    - bank[0][2] -- bank[2][1]
    - bank[0][2] -- bank[2][3]
    - bank[0][5] -- bank[2][1]
    - bank[0][5] -- bank[2][3]
    - bank[2][1] -- bank[3][2]
    - bank[2][3] -- bank[3][2]

    Note that there is no beam between any device on the 0th row with any on the 3rd row. This is because the 2nd row contains security devices, which breaks the second condition.

    ![Example 2](https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg)

    ```
    Input: bank = ["000","111","000"]
    Output: 0
    ```
    **Explanation:** There does not exist two devices located on two different rows.

    ## Constraints

    - m == bank.length
    - n == bank[i].length
    - 1 <= m, n <= 500
    - bank[i][j] is either '0' or '1'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def number_of_beams(self, bank: list[str]) -> int:
            raise NotImplementedError('Implement number_of_beams')

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
