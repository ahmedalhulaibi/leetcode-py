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
    # 1603. Design Parking System

    **Easy** · Design, Simulation, Counting

    Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

    Implement the `ParkingSystem` class:

    - `ParkingSystem(int big, int medium, int small)` Initializes object of the `ParkingSystem` class. The number of slots for each parking space are given as part of the constructor.
    - `bool addCar(int carType)` Checks whether there is a parking space of `carType` for the car that wants to get into the parking lot. `carType` can be of three kinds: big, medium, or small, which are represented by `1`, `2`, and `3` respectively. A car can only park in a parking space of its `carType`. If there is no space available, return `false`, else park the car in that size space and return `true`.

    ## Examples

    ```
    Input
    ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    [[1, 1, 0], [1], [2], [3], [1]]
    Output
    [null, true, true, false, false]

    Explanation
    ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
    parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
    parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
    parkingSystem.addCar(3); // return false because there is no available slot for a small car
    parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
    ```

    ## Constraints

    - `0 <= big, medium, small <= 1000`
    - `carType` is `1`, `2`, or `3`
    - At most `1000` calls will be made to `addCar`

    **Follow up:** Can you implement the `ParkingSystem` class without storing the three capacities in separate variables?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class ParkingSystem:

        def __init__(self, big: int, medium: int, small: int) -> None:
            raise NotImplementedError('Implement __init__')

        def add_car(self, car_type: int) -> bool:
            raise NotImplementedError('Implement add_car')

    practice_exports = {'ParkingSystem': ParkingSystem}
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
