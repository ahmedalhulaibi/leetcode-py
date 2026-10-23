import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_map_sum, run_map_sum
    from solution import MapSum

    return MapSum, assert_map_sum, run_map_sum


@app.cell
def _():
    # Example test case
    operations = ["MapSum", "insert", "sum", "insert", "sum"]
    inputs = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
    expected = [None, None, 3, None, 5]
    return expected, inputs, operations


@app.cell
def _(MapSum, inputs, operations, run_map_sum):
    result, map_sum = run_map_sum(MapSum, operations, inputs)
    print(result)
    map_sum
    return (result,)


@app.cell
def _(assert_map_sum, expected, result):
    assert_map_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
