import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_array, run_num_array
    from solution import NumArray

    return NumArray, assert_num_array, run_num_array


@app.cell
def _():
    # Example test case
    operations = ["NumArray", "sum_range", "update", "sum_range"]
    inputs = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    expected = [None, 9, None, 8]
    return expected, inputs, operations


@app.cell
def _(NumArray, inputs, operations, run_num_array):
    result, num_array = run_num_array(NumArray, operations, inputs)
    print(result)
    num_array
    return (result,)


@app.cell
def _(assert_num_array, expected, result):
    assert_num_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
