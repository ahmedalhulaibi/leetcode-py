import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_matrix_reshape, run_matrix_reshape
    from solution import Solution

    return Solution, assert_matrix_reshape, run_matrix_reshape


@app.cell
def _():
    # Example test case
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    expected = [[1, 2, 3, 4]]
    return c, expected, mat, r


@app.cell
def _(Solution, c, mat, r, run_matrix_reshape):
    result = run_matrix_reshape(Solution, mat, r, c)
    result
    return (result,)


@app.cell
def _(assert_matrix_reshape, expected, result):
    assert_matrix_reshape(result, expected)
    return


if __name__ == "__main__":
    app.run()
