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
    # 849. Maximize Distance to Closest Person

    **Medium** · Array

    You are given an array representing a row of `seats` where `seats[i] = 1` represents a person sitting in the `i<sup>th</sup>` seat, and `seats[i] = 0` represents that the `i<sup>th</sup>` seat is empty **(0-indexed)**.

    There is at least one empty seat, and at least one person sitting.

    Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

    Return *that maximum distance to the closest person*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/10/distance.jpg)

    ```
    Input: seats = [1,0,0,0,1,0,1]
    Output: 2
    Explanation:
    If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.
    ```

    ```
    Input: seats = [1,0,0,0]
    Output: 3
    Explanation:
    If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.
    ```

    ```
    Input: seats = [0,1]
    Output: 1
    ```

    ## Constraints

    - 2 <= seats.length <= 2 * 10^4
    - seats[i] is 0 or 1.
    - At least one seat is empty.
    - At least one seat is occupied.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_dist_to_closest(self, seats: list[int]) -> int:
            raise NotImplementedError('Implement max_dist_to_closest')

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
