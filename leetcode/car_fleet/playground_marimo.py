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
    # 853. Car Fleet

    **Medium** · Array, Stack, Sorting, Monotonic Stack

    There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.

    You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `i<sup>th</sup>` car and `speed[i]` is the speed of the `i<sup>th</sup>` car in miles per hour.

    A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

    A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.

    If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.

    Return the number of car fleets that will arrive at the destination.

    ## Examples

    ```
    Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3
    Explanation:
    - The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
    - The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
    - The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
    ```

    ```
    Input: target = 10, position = [3], speed = [3]
    Output: 1
    Explanation: There is only one car, hence there is only one fleet.
    ```

    ```
    Input: target = 100, position = [0,2,4], speed = [4,2,1]
    Output: 1
    ```

    ## Constraints

    - n == position.length == speed.length
    - 1 <= n <= 10<sup>5</sup>
    - 0 < target <= 10<sup>6</sup>
    - 0 <= position[i] < target
    - All the values of position are **unique**.
    - 0 < speed[i] <= 10<sup>6</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
            raise NotImplementedError('Implement car_fleet')

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
