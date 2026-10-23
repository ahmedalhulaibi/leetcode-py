import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_matrix, run_num_matrix
    from solution import NumMatrix

    return NumMatrix, assert_num_matrix, run_num_matrix


@app.cell
def _():
    # Example test case
    operations = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
    inputs = [
        [[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
        [2, 1, 4, 3],
        [1, 1, 2, 2],
        [1, 2, 2, 4],
    ]
    expected = [None, 8, 11, 12]
    return expected, inputs, operations


@app.cell
def _(NumMatrix, inputs, operations, run_num_matrix):
    result, num_matrix = run_num_matrix(NumMatrix, operations, inputs)
    print(result)
    num_matrix
    return (result,)


@app.cell
def _(assert_num_matrix, expected, result):
    assert_num_matrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
