import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_diagonal_sum, run_diagonal_sum
    from solution import Solution

    return Solution, assert_diagonal_sum, run_diagonal_sum


@app.cell
def _():
    # Example test case
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = 25
    return expected, mat


@app.cell
def _(Solution, mat, run_diagonal_sum):
    result = run_diagonal_sum(Solution, mat)
    result
    return (result,)


@app.cell
def _(assert_diagonal_sum, expected, result):
    assert_diagonal_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
