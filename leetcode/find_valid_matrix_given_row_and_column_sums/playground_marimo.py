import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_restore_matrix, run_restore_matrix
    from solution import Solution

    return Solution, assert_restore_matrix, run_restore_matrix


@app.cell
def _():
    # Example test case
    row_sum = [3, 8]
    col_sum = [4, 7]
    expected = [[3, 0], [1, 7]]
    return col_sum, expected, row_sum


@app.cell
def _(Solution, col_sum, row_sum, run_restore_matrix):
    result = run_restore_matrix(Solution, row_sum, col_sum)
    result
    return (result,)


@app.cell
def _(assert_restore_matrix, col_sum, expected, result, row_sum):
    assert_restore_matrix(result, row_sum, col_sum, expected)
    return


if __name__ == "__main__":
    app.run()
