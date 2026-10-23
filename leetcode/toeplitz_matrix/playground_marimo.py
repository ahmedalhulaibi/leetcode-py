import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_toeplitz_matrix, run_is_toeplitz_matrix
    from solution import Solution

    return Solution, assert_is_toeplitz_matrix, run_is_toeplitz_matrix


@app.cell
def _():
    # Example test case
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    expected = True
    return expected, matrix


@app.cell
def _(Solution, matrix, run_is_toeplitz_matrix):
    result = run_is_toeplitz_matrix(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_is_toeplitz_matrix, expected, result):
    assert_is_toeplitz_matrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
