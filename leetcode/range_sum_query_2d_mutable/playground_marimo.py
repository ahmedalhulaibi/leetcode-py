import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_range_sum_query_2d_mutable, run_range_sum_query_2d_mutable
    from solution import NumMatrix

    return (
        NumMatrix,
        assert_range_sum_query_2d_mutable,
        run_range_sum_query_2d_mutable,
    )


@app.cell
def _():
    # Example test case
    operations = ["NumMatrix", "sum_region", "update", "sum_region"]
    inputs = [
        [[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
        [2, 1, 4, 3],
        [3, 2, 2],
        [2, 1, 4, 3],
    ]
    expected = [None, 8, None, 10]
    return expected, inputs, operations


@app.cell
def _(NumMatrix, inputs, operations, run_range_sum_query_2d_mutable):
    result, matrix_obj = run_range_sum_query_2d_mutable(NumMatrix, operations, inputs)
    print(result)
    matrix_obj
    return (result,)


@app.cell
def _(assert_range_sum_query_2d_mutable, expected, result):
    assert_range_sum_query_2d_mutable(result, expected)
    return


if __name__ == "__main__":
    app.run()
