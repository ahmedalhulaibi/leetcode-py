import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_submatrix, run_largest_submatrix
    from solution import Solution

    return Solution, assert_largest_submatrix, run_largest_submatrix


@app.cell
def _():
    # Example test case
    matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
    expected = 4
    return expected, matrix


@app.cell
def _(Solution, matrix, run_largest_submatrix):
    result = run_largest_submatrix(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_largest_submatrix, expected, result):
    assert_largest_submatrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
