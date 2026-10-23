import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_knight_probability, run_knight_probability
    from solution import Solution

    return Solution, assert_knight_probability, run_knight_probability


@app.cell
def _():
    # Example test case
    n = 3
    k = 2
    row = 0
    column = 0
    expected = 0.0625
    return column, expected, k, n, row


@app.cell
def _(Solution, column, k, n, row, run_knight_probability):
    result = run_knight_probability(Solution, n, k, row, column)
    result
    return (result,)


@app.cell
def _(assert_knight_probability, expected, result):
    assert_knight_probability(result, expected)
    return


if __name__ == "__main__":
    app.run()
