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
    # 1279. Traffic Light Controlled Intersection

    **Easy** · Concurrency, Design

    There is an intersection of two roads. First road is road A where cars travel from North to South in direction 1 and from South to North in direction 2. Second road is road B where cars travel from West to East in direction 3 and from East to West in direction 4.

    ![Example](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1279.Traffic%20Light%20Controlled%20Intersection/images/exp.png)

    There is a traffic light located on each road before the intersection. A traffic light can either be green or red.

    - **Green** means cars can cross the intersection in both directions of the road.
    - **Red** means cars in both directions cannot cross the intersection and must wait until the light turns green.

    The traffic lights cannot be green on both roads at the same time. That means when the light is green on road A, it is red on road B and when the light is green on road B, it is red on road A.

    Initially, the traffic light is **green** on road A and **red** on road B. When the light is green on one road, all cars can cross the intersection in both directions until the light becomes green on the other road. No two cars traveling on different roads should cross at the same time.

    Design a deadlock-free traffic light controlled system at this intersection.

    Implement the function `car_arrived(car_id, road_id, direction, turn_green, cross_car)` where:

    - `car_id` is the id of the car that arrived.
    - `road_id` is the id of the road that the car travels on. Can be 1 (road A) or 2 (road B).
    - `direction` is the direction of the car.
    - `turn_green` is a function you can call to turn the traffic light to green on the current road.
    - `cross_car` is a function you can call to let the current car cross the intersection.

    ## Examples

    ```
    Input: cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]
    Output: [
    "Car 1 Has Passed Road A In Direction 2",    // Traffic light on road A is green, car 1 can cross the intersection.
    "Car 3 Has Passed Road A In Direction 1",    // Car 3 crosses the intersection as the light is still green.
    "Car 5 Has Passed Road A In Direction 2",    // Car 5 crosses the intersection as the light is still green.
    "Traffic Light On Road B Is Green",          // Car 2 requests green light for road B.
    "Car 2 Has Passed Road B In Direction 4",    // Car 2 crosses as the light is green on road B now.
    "Car 4 Has Passed Road B In Direction 3"     // Car 4 crosses the intersection as the light is still green.
    ]
    ```

    ```
    Input: cars = [1,2,3,4,5], directions = [2,4,3,3,1], arrivalTimes = [10,20,30,40,40]
    Output: [
    "Car 1 Has Passed Road A In Direction 2",
    "Traffic Light On Road B Is Green",
    "Car 2 Has Passed Road B In Direction 4",
    "Car 3 Has Passed Road B In Direction 3",
    "Traffic Light On Road A Is Green",
    "Car 5 Has Passed Road A In Direction 1",
    "Traffic Light On Road B Is Green",
    "Car 4 Has Passed Road B In Direction 3"
    ]
    ```

    ## Constraints

    - `1 <= cars.length <= 20`
    - `cars.length = directions.length`
    - `cars.length = arrivalTimes.length`
    - All values of `cars` are unique
    - `1 <= directions[i] <= 4`
    - `arrivalTimes` is non-decreasing

    **Your answer is considered correct if it avoids cars deadlock in the intersection. Turning the light green on a road when it was already green is considered a wrong answer.**

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections.abc import Callable
    from threading import Lock

    class TrafficLight:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def car_arrived(self, car_id: int, road_id: int, direction: int, turn_green: Callable[[], None], cross_car: Callable[[], None]) -> None:
            raise NotImplementedError('Implement car_arrived')

    practice_exports = {'Callable': Callable, 'Lock': Lock, 'TrafficLight': TrafficLight}
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
