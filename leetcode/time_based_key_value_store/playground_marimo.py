import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_time_map_operations, run_time_map_operations
    from solution import TimeMap

    return TimeMap, assert_time_map_operations, run_time_map_operations


@app.cell
def _():
    # Example test case
    operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    inputs = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    expected = [None, None, "bar", "bar", None, "bar2", "bar2"]
    return expected, inputs, operations


@app.cell
def _(TimeMap, inputs, operations, run_time_map_operations):
    result = run_time_map_operations(TimeMap, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_time_map_operations, expected, result):
    assert_time_map_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
