import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_build_matrix, run_build_matrix
    from solution import Solution

    return Solution, assert_build_matrix, run_build_matrix


@app.cell
def _():
    # Example test case
    k = 3
    row_conditions = [[1, 2], [3, 2]]
    col_conditions = [[2, 1], [3, 2]]
    valid = True
    return col_conditions, k, row_conditions, valid


@app.cell
def _(Solution, col_conditions, k, row_conditions, run_build_matrix):
    result = run_build_matrix(Solution, k, row_conditions, col_conditions)
    result
    return (result,)


@app.cell
def _(assert_build_matrix, col_conditions, k, result, row_conditions, valid):
    assert_build_matrix(result, k, row_conditions, col_conditions, valid)
    return


if __name__ == "__main__":
    app.run()
