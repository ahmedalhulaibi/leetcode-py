import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_spiral_matrix, run_spiral_matrix
    from solution import Solution

    return Solution, assert_spiral_matrix, run_spiral_matrix


@app.cell
def _():
    # Example test case
    m = 3
    n = 5
    head_vals = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    expected = [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]
    return expected, head_vals, m, n


@app.cell
def _(Solution, head_vals, m, n, run_spiral_matrix):
    result = run_spiral_matrix(Solution, m, n, head_vals)
    result
    return (result,)


@app.cell
def _(assert_spiral_matrix, expected, result):
    assert_spiral_matrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
