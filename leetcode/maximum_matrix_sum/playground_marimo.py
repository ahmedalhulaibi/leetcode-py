import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_matrix_sum, run_max_matrix_sum
    from solution import Solution

    return Solution, assert_max_matrix_sum, run_max_matrix_sum


@app.cell
def _():
    # Example test case
    matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
    expected = 16
    return expected, matrix


@app.cell
def _(Solution, matrix, run_max_matrix_sum):
    result = run_max_matrix_sum(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_max_matrix_sum, expected, result):
    assert_max_matrix_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
