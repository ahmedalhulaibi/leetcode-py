import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_spiral_matrix_iii, run_spiral_matrix_iii
    from solution import Solution

    return Solution, assert_spiral_matrix_iii, run_spiral_matrix_iii


@app.cell
def _():
    # Example test case
    rows = 1
    cols = 4
    r_start = 0
    c_start = 0
    expected = [[0, 0], [0, 1], [0, 2], [0, 3]]
    return c_start, cols, expected, r_start, rows


@app.cell
def _(Solution, c_start, cols, r_start, rows, run_spiral_matrix_iii):
    result = run_spiral_matrix_iii(Solution, rows, cols, r_start, c_start)
    result
    return (result,)


@app.cell
def _(assert_spiral_matrix_iii, expected, result):
    assert_spiral_matrix_iii(result, expected)
    return


if __name__ == "__main__":
    app.run()
