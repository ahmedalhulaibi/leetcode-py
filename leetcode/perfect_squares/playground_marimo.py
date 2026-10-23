import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_squares, run_num_squares
    from solution import Solution

    return Solution, assert_num_squares, run_num_squares


@app.cell
def _():
    # Example test case
    n = 12
    expected = 3
    return expected, n


@app.cell
def _(Solution, n, run_num_squares):
    result = run_num_squares(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_num_squares, expected, result):
    assert_num_squares(result, expected)
    return


if __name__ == "__main__":
    app.run()
