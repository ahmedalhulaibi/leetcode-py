import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_matrix_score, run_matrix_score
    from solution import Solution

    return Solution, assert_matrix_score, run_matrix_score


@app.cell
def _():
    # Example test case
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    expected = 39
    return expected, grid


@app.cell
def _(Solution, grid, run_matrix_score):
    result = run_matrix_score(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_matrix_score, expected, result):
    assert_matrix_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
