import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_squares, run_count_squares
    from solution import Solution

    return Solution, assert_count_squares, run_count_squares


@app.cell
def _():
    # Example test case
    matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
    expected = 15
    return expected, matrix


@app.cell
def _(Solution, matrix, run_count_squares):
    result = run_count_squares(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_count_squares, expected, result):
    assert_count_squares(result, expected)
    return


if __name__ == "__main__":
    app.run()
