import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_diagonal_order, run_find_diagonal_order
    from solution import Solution

    return Solution, assert_find_diagonal_order, run_find_diagonal_order


@app.cell
def _():
    # Example test case
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]
    return expected, mat


@app.cell
def _(Solution, mat, run_find_diagonal_order):
    result = run_find_diagonal_order(Solution, mat)
    result
    return (result,)


@app.cell
def _(assert_find_diagonal_order, expected, result):
    assert_find_diagonal_order(result, expected)
    return


if __name__ == "__main__":
    app.run()
