import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_trailing_zeroes, run_trailing_zeroes
    from solution import Solution

    return Solution, assert_trailing_zeroes, run_trailing_zeroes


@app.cell
def _():
    # Example test case
    n = 5
    expected = 1
    return expected, n


@app.cell
def _(Solution, n, run_trailing_zeroes):
    result = run_trailing_zeroes(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_trailing_zeroes, expected, result):
    assert_trailing_zeroes(result, expected)
    return


if __name__ == "__main__":
    app.run()
