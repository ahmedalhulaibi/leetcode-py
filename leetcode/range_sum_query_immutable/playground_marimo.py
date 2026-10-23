import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_range_sum_query_immutable, run_range_sum_query_immutable
    from solution import NumArray

    return (
        NumArray,
        assert_range_sum_query_immutable,
        run_range_sum_query_immutable,
    )


@app.cell
def _():
    # Example test case
    operations = ["NumArray", "sumRange", "sumRange", "sumRange"]
    inputs = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    expected = [None, 1, -1, -3]
    return expected, inputs, operations


@app.cell
def _(NumArray, inputs, operations, run_range_sum_query_immutable):
    result = run_range_sum_query_immutable(NumArray, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_range_sum_query_immutable, expected, result):
    assert_range_sum_query_immutable(result, expected)
    return


if __name__ == "__main__":
    app.run()
