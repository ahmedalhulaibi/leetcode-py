import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_set_zeroes, run_set_zeroes
    from solution import Solution

    return Solution, assert_set_zeroes, run_set_zeroes


@app.cell
def _():
    # Example test case
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    return expected, matrix


@app.cell
def _(Solution, matrix, run_set_zeroes):
    result = run_set_zeroes(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_set_zeroes, expected, result):
    assert_set_zeroes(result, expected)
    return


if __name__ == "__main__":
    app.run()
