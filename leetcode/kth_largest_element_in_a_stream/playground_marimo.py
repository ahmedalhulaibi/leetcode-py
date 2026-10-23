import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_largest, run_kth_largest
    from solution import KthLargest

    return KthLargest, assert_kth_largest, run_kth_largest


@app.cell
def _():
    # Example test case
    operations = ["KthLargest", "add", "add", "add", "add", "add"]
    inputs = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    expected = [None, 4, 5, 5, 8, 8]
    return expected, inputs, operations


@app.cell
def _(KthLargest, inputs, operations, run_kth_largest):
    result = run_kth_largest(KthLargest, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_kth_largest, expected, result):
    assert_kth_largest(result, expected)
    return


if __name__ == "__main__":
    app.run()
