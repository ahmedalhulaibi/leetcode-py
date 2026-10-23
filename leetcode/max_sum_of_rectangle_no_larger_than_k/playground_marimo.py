import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_sum_submatrix, run_max_sum_submatrix
    from solution import Solution

    return Solution, assert_max_sum_submatrix, run_max_sum_submatrix


@app.cell
def _():
    # Example test case
    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    expected = 2
    return expected, k, matrix


@app.cell
def _(Solution, k, matrix, run_max_sum_submatrix):
    result = run_max_sum_submatrix(Solution, matrix, k)
    result
    return (result,)


@app.cell
def _(assert_max_sum_submatrix, expected, result):
    assert_max_sum_submatrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
