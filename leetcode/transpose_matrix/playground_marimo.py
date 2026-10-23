import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_transpose, run_transpose
    from solution import Solution

    return Solution, assert_transpose, run_transpose


@app.cell
def _():
    # Example test case
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    return expected, matrix


@app.cell
def _(Solution, matrix, run_transpose):
    result = run_transpose(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_transpose, expected, result):
    assert_transpose(result, expected)
    return


if __name__ == "__main__":
    app.run()
