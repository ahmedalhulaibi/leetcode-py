import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_update_matrix, run_update_matrix
    from solution import Solution

    return Solution, assert_update_matrix, run_update_matrix


@app.cell
def _():
    # Example test case
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    return expected, mat


@app.cell
def _(Solution, mat, run_update_matrix):
    result = run_update_matrix(Solution, mat)
    result
    return (result,)


@app.cell
def _(assert_update_matrix, expected, result):
    assert_update_matrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
