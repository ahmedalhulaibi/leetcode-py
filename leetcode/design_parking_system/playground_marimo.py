import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_parking_system, run_parking_system
    from solution import ParkingSystem

    return ParkingSystem, assert_parking_system, run_parking_system


@app.cell
def _():
    # Example test case
    operations = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    inputs = [[1, 1, 0], [1], [2], [3], [1]]
    expected = [None, True, True, False, False]
    return expected, inputs, operations


@app.cell
def _(ParkingSystem, inputs, operations, run_parking_system):
    result, system = run_parking_system(ParkingSystem, operations, inputs)
    print(result)
    system
    return (result,)


@app.cell
def _(assert_parking_system, expected, result):
    assert_parking_system(result, expected)
    return


if __name__ == "__main__":
    app.run()
