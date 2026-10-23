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
    # 365. Water and Jug Problem

    **Medium** · Math, Depth-First Search, Breadth-First Search, Greatest Common Divisor

    You are given two jugs with capacities `x` liters and `y` liters. You have an infinite water supply. Return *whether the total amount of water in both jugs may reach* `target` *using the following operations*:

    - Fill either jug completely with water.
    - Completely empty either jug.
    - Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.

    ## Examples

    ```
    Input: x = 3, y = 5, target = 4
    Output: true
    Explanation:
    Fill the 5-liter jug (0, 5). Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2). Empty the 3-liter jug (0, 2). Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0). Fill the 5-liter jug again (2, 5). Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is full. This leaves 4 liters in the 5-liter jug (3, 4). Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0, 4).
    ```

    ```
    Input: x = 2, y = 6, target = 5
    Output: false
    ```

    ```
    Input: x = 1, y = 2, target = 3
    Output: true
    Explanation: Fill both jugs. The total amount of water in both jugs is equal to 3 now.
    ```

    ## Constraints

    - `1 <= x, y, target <= 10^3`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_measure_water(self, x: int, y: int, target: int) -> bool:
            raise NotImplementedError('Implement can_measure_water')

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
