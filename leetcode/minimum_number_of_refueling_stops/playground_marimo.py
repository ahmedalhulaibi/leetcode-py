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
    # 871. Minimum Number of Refueling Stops

    **Hard** · Array, Dynamic Programming, Greedy, Heap (Priority Queue)

    A car travels from a starting position to a destination which is `target` miles east of the starting position.

    There are gas stations along the way. The gas stations are represented as an array `stations` where `stations[i] = [position<sub>i</sub>, fuel<sub>i</sub>]` indicates that the `i<sup>th</sup>` gas station is `position<sub>i</sub>` miles east of the starting position and has `fuel<sub>i</sub>` liters of gas.

    The car starts with an infinite tank of gas, which initially has `startFuel` liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

    Return *the minimum number of refueling stops the car must make in order to reach its destination*. If it cannot reach the destination, return `-1`.

    Note that if the car reaches a gas station with `0` fuel left, the car can still refuel there. If the car reaches the destination with `0` fuel left, it is still considered to have arrived.

    ## Examples

    ```
    Input: target = 1, startFuel = 1, stations = []
    Output: 0
    Explanation: We can reach the target without refueling.
    ```

    ```
    Input: target = 100, startFuel = 1, stations = [[10,100]]
    Output: -1
    Explanation: We can not reach the target (or even the first gas station).
    ```

    ```
    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    Output: 2
    Explanation: We start with 10 liters of fuel.
    We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
    Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
    and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
    We made 2 refueling stops along the way, so we return 2.
    ```

    ## Constraints

    - `1 <= target, startFuel <= 10^9`
    - `0 <= stations.length <= 500`
    - `1 <= position<sub>i</sub> < position<sub>i+1</sub> < target`
    - `1 <= fuel<sub>i</sub> < 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_refuel_stops(self, target: int, start_fuel: int, stations: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_refuel_stops')

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
