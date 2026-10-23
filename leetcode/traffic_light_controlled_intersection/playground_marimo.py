import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_traffic_light, run_traffic_light
    from solution import TrafficLight

    return TrafficLight, assert_traffic_light, run_traffic_light


@app.cell
def _():
    # Example test case
    operations = [
        "TrafficLight",
        "car_arrived",
        "car_arrived",
        "car_arrived",
        "car_arrived",
        "car_arrived",
    ]
    inputs = [[], [1, 1, 2], [3, 1, 1], [5, 1, 2], [2, 2, 4], [4, 2, 3]]
    expected = [
        "Car 1 Has Passed Road A In Direction 2",
        "Car 3 Has Passed Road A In Direction 1",
        "Car 5 Has Passed Road A In Direction 2",
        "Traffic Light On Road B Is Green",
        "Car 2 Has Passed Road B In Direction 4",
        "Car 4 Has Passed Road B In Direction 3",
    ]
    return expected, inputs, operations


@app.cell
def _(TrafficLight, inputs, operations, run_traffic_light):
    result, light = run_traffic_light(TrafficLight, operations, inputs)
    print(result)
    light
    return (result,)


@app.cell
def _(assert_traffic_light, expected, result):
    assert_traffic_light(result, expected)
    return


if __name__ == "__main__":
    app.run()
