import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rotate, run_rotate
    from solution import Solution

    return Solution, assert_rotate, run_rotate


@app.cell
def _():
    # Example test case
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    return expected, matrix


@app.cell
def _(Solution, matrix, run_rotate):
    result = run_rotate(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_rotate, expected, result):
    assert_rotate(result, expected)
    return


if __name__ == "__main__":
    app.run()
